from mifun import Map, Print, Range, Table

Map(lambda x: Print(x * 7, {"end": " "}), range(10))
Print()
var = Map(lambda x: x * 3.14 + 5, Range(10))
Print(*var, {"sep": ", "})
Print(Table(*var))
