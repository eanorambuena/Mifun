from mifun import Cos, I, X, Evens, Odds, Print, Green, String
from scopes import scope, switch
import math

a = 0.1
b = 9

Weistrass = I * 0
for n in range(3):
    Weistrass += Cos[X * (b ** n * math.pi)] * (a ** n)

for i in range(10):
    switch(i, {
        Odds: Print[X * 3 + 1],
        Evens: scope({
            (lambda x: print(f"Weistrass({x}) = ", end = "")): i / 3,
            Print[Green[String[Weistrass]]]: i / 3
        }) 
    })
