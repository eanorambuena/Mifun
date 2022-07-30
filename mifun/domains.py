import types

from mifun.utils import *

class Domain():
    def __init__(self, contain_function = is_real, name = "Domain"):
        if type(contain_function) == list:
            list_domain = contain_function
            def contain_function(x):
                return x in list_domain
            name = f"Domain({list_domain})"

        # if is Function class:
        if not isinstance(contain_function, (types.FunctionType, types.BuiltinFunctionType)):
            self.contain_function = contain_function.domain.contain_function
            self.name = contain_function.domain.name
            return
            
        self.contain_function = contain_function
        self.name = name
    def __contains__(self, x):
        return self.contain_function(x)
    def __add__(self, other):
        def new_f(x):
            return self.contain_function(x) or other.contain_function(x)
        return Domain(new_f, f"{self.name} + {other.name}")
    def __sub__(self, other):
        def new_f(x):
            return self.contain_function(x) and not other.contain_function(x)
        return Domain(new_f, format_function(self, other, "-"))
    def __mul__(self, other):
        def new_f(x):
            return self.contain_function(x) and other.contain_function(x)
        return Domain(new_f, format_function(self, other, "*"))
    def __pow__(self, other):
        def new_f(x):
            return self.contain_function(x[0]) and other.contain_function(x[1])
        return Domain(new_f, format_function(self, other, "**"))
    @property
    def short_name(self):
        result = self.name
        result = result.replace("Reals * ", "").replace(" * Reals", ""). replace("Reals + ", "").replace(" + Reals", "")
        result = result.replace("Intergers * Reals", "Intergers").replace("Reals * Intergers", "Intergers")
        return symmetric_strip(result)
    def __eq__(self, other):
        return self.short_name == other.short_name
    def __getitem__(self, dimension):
        def new_f(x):
            return all(i in self for i in x)
        if " " in self.name:
            name = f"({self.name})[{dimension}]"
        else:
            name = f"{self.name}[{dimension}]"
        return Domain(new_f, name)
    def __repr__(self): 
        return self.short_name
    def __str__(self):
        return repr(self)

Universe    = Domain(universal_truth,   "Universe")
EmptySet    = Domain(universal_falsity, "EmptySet")
Intergers   = Domain(is_integer,        "Intergers")
Reals       = Domain(is_real,           "Reals")
Positive    = Domain(is__positive,      "Positive")
Negative    = Domain(is_negative,       "Negative")
Zero        = Domain([0],               "Zero")
Callables   = Domain(callable,          "Callables")
Strings     = Domain(is_string,         "Strings")

NonNegative = Positive + Zero
NonNegative.name = "NonNegative"

Naturals    = Intergers * NonNegative
Naturals.name = "Naturals"

ForDomain   = Domain(for_domain_function, "ForDomain")
