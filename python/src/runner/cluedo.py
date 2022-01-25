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


if __name__ == "__main__":
    print("hello world")

