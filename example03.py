from mifun import Cos, I, X, Function, Evens, Odds, Print
from scopes import scope, switch
import math

a = 0.1
b = 9

Weistrass = I * 0
for n in range(3):
    Weistrass += Cos[X * (b ** n * math.pi)] * (a ** n)

for i in range(10):
    switch(i, 
        {
            Odds: Print[X * 2],
            Evens: scope(
                {
                    (lambda x: print(f"Weistrass({x}) = ", end = "")): i / 3,
                    Print[Weistrass]: i / 3,
                    Print["hola"]: None
                }
            )
        }
    )
