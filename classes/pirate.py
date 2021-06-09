class Pirate:
    def __init__(self, name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.dex = 5

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def attack(self, ninja):
        ninja.health -= self.strength
        return self


class RumPirate(Pirate):
    def __init__(self, name):
        super().__init__(name)

    def alcoholism(self):
        self.dex -= 1
        self.health += self.health * .1
        self.strength += 20
        return self

    def gassy(self, target):
        print(f"{target.name} lost {target.health} health by {self.name}.")
        return self

    def taunt(self, ninja):
        ninja.strength -= 5
        print("you fight like my grandmother and she still fights better than you!")
