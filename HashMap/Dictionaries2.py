d={1:6,2:7,3:8,4:9,5:10,list:[1,2,3,4,5,6],"donkey":"modu",dict:{1:1}}

#access the key's value
print(d[list]) # list is a keyword
print(d["donkey"]) #donkey is not a keyword

#access the key's value using get(keyName) function

print(d.get(1)) #if it don't find a value the default value be None
print(d.get(0,"Not found")) #if it don't find a value the default value be Not Found

#access all keys from dict
print(d.keys())

#access all values from dict
print(d.values())

#access all keys:values from dict
print(d.items())

#access all keys from dict using for loop
for i in d:
    print(i)
#access all keys:values from dict using for loop
for i in d:
    print(i,d[i])

#access all values from dict using for loop
for i in d:
    print(d[i])
#or
for i in d.values():
    print(i)

#check key is present in dict
print("manshu" in d)
print("donkey" in d)



