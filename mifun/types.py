def get_digits(*args):
    digits = []
    for arg in args:
        tail = str(float(arg)).split(".")[1]
        digits.append(len(tail))
    return digits


class NumberType(float):

    def __init__(self, value) -> None:
        self = float(value)

    def __add__(*args):
        return NumberType(round(sum(args), max(get_digits(*args))))

    def __sub__(*args):
        return NumberType(round(args[0] - sum(args[1:]), max(get_digits(*args))))

    def __mul__(*args):
        result = 1
        for arg in args:
            result *= arg
        return NumberType(round(result, sum(get_digits(*args))))
    