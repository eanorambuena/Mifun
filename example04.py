from mifun import Map, Print

Map(lambda x: Print(x * 7, {"end": " "}), range(10))
Print()
var = Map(lambda x: x * 3.14, range(10))
Print(*var, {"sep": ", "})
