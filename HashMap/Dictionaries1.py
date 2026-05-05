dict={"a":1,"b":2,"c":3}
print(dict)
#copy()
dict2=dict.copy()
print(dict2)
#id()
print(id(dict),id(dict2))

#create a dict with a help of list and tuples
#d=dict([("a","1"), ("b","2"), ("c","3")])
#print(d)

#create a dict using fromKeys(iterable,defaultValue)
d=dict.fromkeys(["a","b","c"])
print(d)
d=dict.fromkeys(["a","b","c"],10)
print(d)
