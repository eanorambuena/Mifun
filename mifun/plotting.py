from prettytable import PrettyTable as pt

class Metadata():
    def __init__(self, title = "Outputs"):
        self.title = title

def tabulate(args_list):
    # returns a table in str
    tb = pt()
    title = "Output"

    if type(args_list[-1]) == Metadata:
        title = args_list[-1].title
        args_list = args_list[:-1]

    items = [repr(x) for x in args_list]
    tb.field_names = [f"{title} {i}" for i in range(0, len(items))] 
    tb.add_row([repr(x) for x in args_list])
    return tb

def v_tabulate(args_list):
    # returns a table in str
    tb = pt()
    tb.field_names = ["Outputs"]

    if type(args_list[-1]) == Metadata:
        tb.field_names = [args_list[-1].title]
        args_list = args_list[:-1]

    items = [repr(x) for x in args_list]
    for i in range(0, len(items)):
        tb.add_row([items[i]])
    return tb
