import numpy as np

class Field(np.ndarray):
    def __init__(self, array_of_functions, name = "Field"):
        self = np.array(array_of_functions)
        self.name = name

