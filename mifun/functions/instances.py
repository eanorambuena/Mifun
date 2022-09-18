import math
import mifun.domains as            dom
from   mifun.functions.core import Function
from   mifun.utils import          *
from   mifun.plotting import       *
from   mifun.scopes import         scope
from   mifun.types import          NumberType

def call_catching_kwargs(function, x):
    try:
        if x not in dom.Iterables:
            x = [x]

        if  len(x) == 0:
            return function()

        kwargs = x[-1]
        args = x[0:-1]
        return function(*args, **kwargs)
    except TypeError:
        if type(x) == list:
            return function(x[0])
        return function(x)

# Mathematical Functions
I        = Function(Constant1,           dom.Reals,                    "I")
X        = Function(x,                   dom.Reals,                    "X")
Sin      = Function(math.sin,            dom.Reals,                    "Sin")
Cos      = Function(math.cos,            dom.Reals,                    "Cos")
Tan      = Function(math.tan,            dom.Reals - (Cos == 0),       "Tan")
Sqrt     = Function(math.sqrt,           dom.Reals * dom.NonNegative,  "Sqrt")
Sum      = Function(sum,                 dom.Reals[2],                 "Sum")
Element  = Function(lambda x, y: x in y, dom.Universe[2],               "Element")

# Actional Functions
Add = Function(lambda x, y: x + y, dom.Universe[2], "Add")
For = Function(for_function,       dom.ForDomain,   "For")

def summatory(x):
    term_function = x[0]
    n = x[1]

    def new_f(y):
        return term_function(y[0]) + y[1]
        
    if len(x) == 3:
        return For(new_f, range(0, n), x[2])
    return For(new_f, range(0, n), 0)

Summatory = Function(summatory, dom.Callables ** dom.Intergers, "Summatory")

# Plotting Functions
Title         = Function(Metadata,   dom.Strings,  "Title")
Table         = Function(tabulate,   dom.Universe, "Table")
VerticalTable = Function(v_tabulate, dom.Universe, "VerticalTable")

Print         = Function(lambda x: call_catching_kwargs(print, x), name = "Print", catch_kwargs = True)
Print0        = Function(lambda x: print(x, end = ""),             name = "Print0")

# Style Functions
Black  = Function(lambda x: black  + x + white, dom.Strings, "Black")
Red    = Function(lambda x: red    + x + white, dom.Strings, "Red")
Green  = Function(lambda x: green  + x + white, dom.Strings, "Green")
Blue   = Function(lambda x: blue   + x + white, dom.Strings, "Blue")
Yellow = Function(lambda x: yellow + x + white, dom.Strings, "Yellow")
Cyan   = Function(lambda x: cyan   + x + white, dom.Strings, "Cyan")
Purple = Function(lambda x: purple + x + white, dom.Strings, "Purple")
White  = Function(lambda x: white  + x,         dom.Strings, "White")

# Type Functions
Int    = Function(int,    dom.Reals,    "Int")
Float  = Function(float,  dom.Reals,    "Float")
String = Function(str,    dom.Universe, "String")

# Scope Functions
Scope  = Function(lambda x: Function(scope(x)),    dom.Dictionaries,               "Scope")
Map    = Function(lambda x: list(map(x[0], x[1])), dom.Callables ** dom.Iterables, "Map")

# Generative Functions
Range  = Function(lambda x: [NumberType(n) for n in range(x)], dom.Intergers, "Range")
