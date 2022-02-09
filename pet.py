

class Pet():

    def __init__(self, name, type, tricks, health, energy):

        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy =+ 25
        print(f"{self.name} sleeps, ENERGY: {self.energy}" )
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} eats, ENERGY: {self.energy} HEALTH: {self.health}")
        return self
    def play(self):
        self.health += 5
        self.energy -= 5
        print(f"{self.name} plays, HEALTH: {self.health} ENERGY: {self.energy}")
        return self
    def noise(self):
        print("bark bark dude")

class BigPet(Pet):

    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)

    def shot1(self):
        super().play()
        return self