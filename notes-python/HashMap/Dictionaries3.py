d={1:6,2:7,3:8,4:9,5:10,list:[1,2,3,4,5,6],"donkey":"modu",dict:{1:1}}
print(d)
#Adding element in dict
d["anju"]=["mother"]
print(d)
#Updating values in dict
d["anju"]="mother of manshu"
print(d)
#Updating dict using update function
temp={1:10,2:20,"manshu":"simple man"}
d.update(temp)
print(d)

#Deleting data using pop(1 arg)
d.pop(1) #returns key:value of pop
print(d)

#Deleting data using del[key]
del d[2]
print(d)
#Deleting all keys using clear function
d.clear()
print(d)








