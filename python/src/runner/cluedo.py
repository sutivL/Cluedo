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
        # Check if inputs are correct
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
        # Read user input
        print("\nMurder: ", end='')
        murder = int(input())
        print("Murder weapon: ", end='')
        murderWeapon = int(input())
        print("Murder room: ", end='')
        murderRoom = int(input())

        correct = gameLogic.guess(murder, murderWeapon, murderRoom)
        # Check if won
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
    # Recursion to play again
    if again == 'j' or again == 'J':
        play()


if __name__ == "__main__":
    # Create game objects
    persons = [
        Person("Scarlett", "Miss", 25, "Blonde Haare"),
        Person("Mustard", "Colonel", 55, "Schnurrbart"),
        Person("White", "Miss", 50, "Kochmütze"),
        Person("Plum", "Professor", 55, "Brille"),
        Person("Green", "Pastor", 60, "Glatze"),
        Person("Peacock", "Miss", 65, "Diadem")
    ]
    weapons = [
        Weapon("Dolch", 250, 15, "erstechen"),
        Weapon("Kerzenständer", 500, 45, "erschlagen"),
        Weapon("Rohr", 450, 35, "erschlagen"),
        Weapon("Seil", 400, 1500, "erdrosseln"),
        Weapon("Rohrzange", 800, 50, "erschlagen"),
        Weapon("Pistole", 450, 40, "erschiessen")
    ]
    rooms = [
        Room("Halle", 25, 25, 0, 3, "Platten"),
        Room("Lounge", 15, 15, 5, 1, "Teppich"),
        Room("Essraum", 20, 20, 4, 2, "Parkett"),
        Room("Küche", 25, 30, 15, 4, "Platten"),
        Room("Ballsaal", 100, 5, 8, 2, "Parkett"),
        Room("Musikzimmer", 25, 5, 10, 1, "Platten"),
        Room("Billiardzimmer", 25, 4, 6, 2, "Parkett"),
        Room("Bibliothek", 40, 4, 4, 2, "Teppich"),
        Room("Studierzimmer", 20, 5, 5, 1, "Teppich")
    ]

    print("########################################################################")
    # Print all persons
    print("Persons:")
    for i in range(len(persons)):
        print(str(i) + " ", end='')
        persons[i].print()
    # Print all weapons
    print("\nWeapons:")
    for i in range(len(weapons)):
        print(str(i) + " ", end='')
        weapons[i].print()
    # Print all rooms
    print("\nRooms:")
    for i in range(len(rooms)):
        print(str(i) + " ", end='')
        rooms[i].print()

    print("########################################################################")
    # Start game
    play()
    print("\nBye!")
