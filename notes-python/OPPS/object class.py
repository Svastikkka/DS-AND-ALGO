class circle(object):
    def __init__(self,radius):
        self.__radius=radius
        print(self.__radius)
    def __str__(self):
        return "This is circle class"
c=circle(3)
print(c)