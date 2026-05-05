class vehicle:
    def __init__(self,color,max_speed):
        self.color=color
        self.max_speed=max_speed
class car(vehicle):
    def __init__(self,color,max_speed,numOfGears,isConvertible):
        super().__init__(color,max_speed)
        self.numOfGears=numOfGears
        self.isConvertible=isConvertible
    def printCar(self):
        print(self.isConvertible)
        print(self.numOfGears)
        print(self.color)
        print(self.max_speed)
s=car("red",100,3,"yes")
s.printCar()