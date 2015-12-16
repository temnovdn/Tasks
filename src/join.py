def join(keys, values):
    """Receives two lists (list of keys and list of values) and joins them into a dictionary.
    Values for keys[i>len(values)] will be set as None.
    Values for values[i>len(keys)] will be discarded.
    :parameter keys
    :parameter values
    """
    dictionary = {}
    for index in range(len(keys)):
        if index < len(values):
            dictionary[keys[index]] = values[index]
        else:
            dictionary[keys[index]] = None
    return dictionary
