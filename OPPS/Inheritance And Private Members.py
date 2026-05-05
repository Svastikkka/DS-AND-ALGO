class people:
    def __init__(self,name,age):
        self.__name=name
        self.age=age


        
    def getName(self):
        return  self.__name
    def setName(self,name):
        self.__name=name

class gender(people):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender=gender
    def printInfo(self):
        print(self.getName())
        print(self.gender)
        print(self.age)
g=gender("manshu",22,"Male")
g.printInfo()

