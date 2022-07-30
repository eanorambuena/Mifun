from prettytable import PrettyTable as pt

def tabulate(args_list):
    # returns a table in str
    tb = pt()
    tb.field_names = [repr(x) for x in args_list]
    return tb
