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


class GameLogic:
    def __init__(self):
        super(GameLogic, self).__init__()

    def initialise(self, persons, weapons, rooms):
        self.murder = randint(0, len(persons))
        self.murderWeapon = randint(0, len(weapons))
        self.murderRoom = randint(0, len(rooms))

    def guess(self, murder, murderWeapon, murderRoom):
        correct = 0
        if murder == self.murder:
            correct += 1
        if murderWeapon == self.murderWeapon:
            correct += 1
        if murderRoom == self.murderRoom:
            correct += 1
        return correct


def play():
    gameLogic = GameLogic()
    gameLogic.initialise(persons, weapons, rooms)
    print("________________________________________________________________________")
    print("You have 5 guesses to win the game!")
    i = 5
    while i > 0:
        print("\nMurder: ", end='')
        murder = int(input())
        print("Murder weapon: ", end='')
        murderWeapon = int(input())
        print("Murder room: ", end='')
        murderRoom = int(input())

        correct = gameLogic.guess(murder, murderWeapon, murderRoom)
        if correct == 3:
            print("You guessed all 3 correctly!")
            print("Game WON!")
            break
        else:
            i -= 1
            print("You have guessed " + str(correct) + " right, try again!")
            print("You have " + str(i) + " tries left.")
            if i == 0:
                print("Game LOSE!")

    print("\nPlay again? (j/n)", end='')
    again = input()
    if again == 'j' or again == 'J':
        play()


if __name__ == "__main__":
    print("hello world")

