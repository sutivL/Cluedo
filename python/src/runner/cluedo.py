from random import randint


class Person:
    def __init__(self, name, salutation, age, characteristic):
        super(Person, self).__init__()
        self.name = name
        self.salutation = salutation
        self.age = age
        self.characteristic = characteristic

    def print(self):
        print("name: " + self.name
              + ", salutation: " + self.salutation
              + ", age: " + str(self.age)
              + ", characteristic: " + self.characteristic)


class Room:
    def __init__(self, designation, width, height, numberOfWindows, numberOfDoors, floorType):
        super(Room, self).__init__()
        self.designation = designation
        self.width = width
        self.height = height
        self.numberOfWindows = numberOfWindows
        self.numberOfDoors = numberOfDoors
        self.floorType = floorType

    def print(self):
        print("designation: " + self.designation
              + ", width: " + str(self.width)
              + ", height: " + str(self.height)
              + ", number of windows: " + str(self.numberOfWindows)
              + ", number of doors: " + str(self.numberOfDoors)
              + ", floor type: " + self.floorType)


class Weapon:
    def __init__(self, designation, weight, length, killingType):
        super(Weapon, self).__init__()
        self.designation = designation
        self.weight = weight
        self.length = length
        self.killingType = killingType

    def print(self):
        print("designation: " + self.designation
              + ", weight: " + str(self.weight)
              + ", length: " + str(self.length)
              + ", killing type: " + self.killingType)


if __name__ == "__main__":
    print("hello world")

