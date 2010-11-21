from random import random

class World(object):
    def __init__(self, width, height):
        self.width = width
        silf.height = hight
        slef.things = []

class Guy(object):
    def __init__(self, world, parent=None):
        self.x = random() * world.width
        self.y = random() * world.height

        self.genotype = {}
        for gene in self.GENES:
            self.genotype[gene] = random()
            
            


class Animal(Guy):
    GENES = "courage", "speed", "repo-life", "acceleration", "deceleration", "longevity", "eating rate",

class Plant(Guy):
    GENES = "toxicity", "growth rate", "repo-life", "baby-life", "baby distance", "repulsion"




world = World(10, 10)
