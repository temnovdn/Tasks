def join(keys, values):
    dictionary = {}
    for key in keys:
        index = keys.index(key)
        if index < len(values):
            value = values[index]
            dictionary[key] = value
        else:
            dictionary[key] =  "None"
    return dictionary