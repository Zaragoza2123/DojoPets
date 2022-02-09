from pet import *


class Ninja():

    def __init__(self, first_name, last_name, treats, pet_food, pet, pet2):

        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet 
        self.pet2 = pet2

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

    def shot(self):
        self.pet2.shot1()
        return self



lilchompchomp = Pet("Lil Chomp Chomp", "wolf", "devour", 90, 50)
bigchompchomp = BigPet("Big Chomp Chomp", "wolf", "consume", 150, 100)
Yote = Ninja("Yote", "San", "cows leg", "taco bell", lilchompchomp, bigchompchomp)
Yote.feed().walk().bathe()
Yote.shot()
