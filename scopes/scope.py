class ScopeVariable():
    pass


class Protect():
    lines = 0

    def __init__(self, function):
        self.line = Protect.lines
        Protect.lines += 1
        self.function = function

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)

Null = ScopeVariable()

def scope(dictionary: dict):
    def new_f():
        for key in dictionary.keys():
            if dictionary[key] is not Null:
                if type(dictionary[key]) == tuple:
                    key(*dictionary[key])
                elif type(dictionary[key]) == dict:
                    key(**dictionary[key])
                else:
                    key(dictionary[key])
    return new_f

if __name__ == "__main__":
    scope(
        {
            Protect(print): 2,
            Protect(print): Null,
            Protect(input): "Enter a number: ",
            Protect(print): 3
        }
    )
