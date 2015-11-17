from lists import join


keys1 = ['key1', 'key2', 'key3', 'key4']
values1 = ['val1', 'val2', 'val3']
keys2 = ['key1', 'key2']

dict1 = join(keys1,values1)
dict2 = join(keys2, values1)

print(dict1)
print(dict2)