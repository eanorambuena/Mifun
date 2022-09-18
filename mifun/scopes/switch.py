def switch(variable, dictionary: dict):
    for value in dictionary.values():
        if not callable(value):
            return
    if variable in dictionary.keys():
        try:
            return dictionary[variable](variable)
        except TypeError:
            return dictionary[variable]()
    
    try:
        for key in dictionary.keys():
            if variable in key:
                try:
                    return dictionary[key](variable)
                except TypeError:
                    return dictionary[key]()
    except TypeError:
        pass
