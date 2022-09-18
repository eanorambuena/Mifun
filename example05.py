from mifun import Print, Cos, Var, Reals
from math import pi

x = Var("x", Reals[3], 0)
y = Var("y", Reals[3], 1)
z = Var("z", Reals[3], 2)
f = x ** 7 + z ** 2 * 5 - x * 3 + 1 + Cos[y]
Print(f(3, pi/2, 10))
