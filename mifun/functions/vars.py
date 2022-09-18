import mifun.domains as dom
from mifun.functions.core import Function
from mifun.functions.instances import X


class Var(Function):

    def __init__(self, name = "Var"):
        super().__init__(X, dom.Reals, name)

    def __repr__(self):
        return f"Var({self.name})"
