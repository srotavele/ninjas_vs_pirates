class Ninja:

    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, pirate):
        pirate.health -= self.strength
        return self


class ZombieNinja(Ninja):
    def __init__(self, name):
        super().__init__(name)

    def bite(self, pirate):
        pirate.health -= 50
        print("BRRRRAAAAIIIINNNNNSSSSS")
        return self
