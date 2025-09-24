import random


class Hat:
    houses = ["Griffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



Hat.sort("Harry")