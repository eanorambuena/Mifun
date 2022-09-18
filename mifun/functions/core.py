import  mifun.domains as      dom
from    mifun.utils import    *
from    mifun.plotting import *

class Function():

    def __init__(self, f, domain = dom.Universe, name = "Function"):
        self.f = f
        self.domain = domain
        self.name = name

    def __call__(self, *args):
        x = list(args)
        if len(args) == 1:
            x = args[0]
        if not (x in self.domain):
            raise ValueError(f"Value out of domain: {self.domain}")
        if type(self.f) == list:
            result = []
            for f in self.f:
                result.append(f(x))
            return result
        else:
            return self.f(x)

    def __add__(self, other):
        if other in dom.Reals:
            def ConstantOther(x):
                return other
            return self + Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) + other.f(x)

        return Function(new_f, self.domain * other.domain, f"{self.name} + {other}")

    def __key(self):
        return tuple(v for k, v in sorted(self.__dict__.items()))

    def __hash__(self):
        return hash(self.__key)

    def __sub__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self - Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) - other.f(x)

        if " " in other.name:
            name = f"{self.name} - ({other})"
        else:
            name = f"{self.name} - {other}"
        return Function(new_f, self.domain * other.domain, name)

    def __mul__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self * Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) * other.f(x)

        name = format_function(self, other, "*")
        return Function(new_f, self.domain * other.domain, name)

    def __pow__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self ** Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) ** other.f(x)

        name = format_function(self, other, "**")
        return Function(new_f, self.domain * other.domain, name)

    def __truediv__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self / Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) / other.f(x)

        name = format_function(self, other, "/")
        return Function(new_f, self.domain * other.domain - (other == 0), name)

    def __neg__(self):

        def new_f(x):
            return -self.f(x)

        if " " in self.name:
            name = f"-({self.name})"
        else:
            name = f"-{self.name}"
        return Function(new_f, self.domain, name)

    def __getitem__(self, other): #compose
        if " " in self.name:
            name = f"({self.name})[{other}]"
        else:
            name = f"{self.name}[{other}]"
        
        if type(other) != Function:

            def new_f(x):
                return other

            return Function(new_f, self.domain, name)

        def new_f(x):
            return self.f(other.f(x))
        
        return Function(new_f, other.domain * (other % self.domain), name)

    def __eq__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self == Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) == other.f(x)

        return dom.Domain(new_f, f"({self.name} == {other})")

    def __ne__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self != Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) != other.f(x)

        return dom.Domain(new_f, f"({self.name} != {other})")

    def __lt__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self < Function(ConstantOther, name = str(other))
            
        def new_f(x):
            return self.f(x) < other.f(x)

        return dom.Domain(new_f, f"({self.name} < {other})")

    def __le__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self <= Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) <= other.f(x)

        return dom.Domain(new_f, f"({self.name} <= {other})")

    def __gt__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self > Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) > other.f(x)

        return dom.Domain(new_f, f"({self.name} > {other})")

    def __ge__(self, other):
        if other in dom.Reals:

            def ConstantOther(x):
                return other

            return self >= Function(ConstantOther, name = str(other))

        def new_f(x):
            return self.f(x) >= other.f(x)

        return dom.Domain(new_f, f"({self.name} >= {other})")

    def __mod__(self, domain):

        def new_f(x):
            return self.f(x) in domain
            
        if domain == dom.Positive:
            name = f"({self.name} > 0)"
        elif domain == dom.Negative:
            name = f"({self.name} < 0)"
        elif domain == dom.NonNegative:
            name = f"({self.name} >= 0)"
        else:
            name = format_function(self, domain, "%")
        return dom.Domain(new_f, name)

    @property
    def short_name(self):
        result = self.name
        result = result.replace("I * 0.0 + ", "").replace("I * 0.0 - ", "-").replace("I * 0 + ", "").replace("I * 0 - ", "-")
        result = result.replace(" * I * 1.0", "").replace(" * I * 1", "").replace(" + I * 1.0", "").replace(" + I * 1", "")
        result = result.replace(" ** 1.0", "").replace(" ** 1", "").replace(" * 1.0", "").replace(" * 1", "")
        return result.strip()

    def __repr__(self):
        return self.short_name

    def __str__(self):
        return repr(self)
