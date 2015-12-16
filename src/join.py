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

a = [0, 1, 2, 3, 4, 5]
b = [0, 1, 2, 3, 4, 5, 6]

print(join(a, b))
