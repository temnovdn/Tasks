def join(keys, values):
    """Receives two lists (list of keys and list of values) and joins them into a dictionary.
    Values for keys[i>len(values) will be set as None.
    Values for values[i>len(keys)] will be discarded.
    :parameter keys
    :parameter values
    """
    dictionary = {}
    for key in keys:
        index = keys.index(key)
        if index < len(values):
            value = values[index]
            dictionary[key] = value
        else:
            dictionary[key] = None
    return dictionary
