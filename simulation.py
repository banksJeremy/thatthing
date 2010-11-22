#!/usr/bin/env python3.1
from random import random

class World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.things = []
    
    def populate(self, types):
        """Populate the simulation with an individual per provided species.
        
        For example, you could call .populate([Animal, Plant, Plant, Plant])
        to have an animal and three plants. You might write this more clearly
        as .populate([Animal] + 3 * [Plant])."""
        
        for species in types:
            self.things.append(species(self))
    
    def tick(self):
        "Advance the simulation by a frame."
        
        # TODO: change the properties of the things in this simulation

class Guy(object):
    radius = 5
    
    def __init__(self, world, parent=None):
        """Initializes this guy to a random position in the world and with
        a genotype randomly generated or mutated from a parent."""
        
        self.x = random() * world.width
        self.y = random() * world.height
        
        self.genotype = {}
        for gene in self.GENES:
            self.genotype[gene] = random()

class Animal(Guy):
    GENES = "courage", "speed", "repo-life", "acceleration", "deceleration", "longevity", "eating rate",    
    color = "orange"

class Plant(Guy):
    GENES = "toxicity", "growth rate", "repo-life", "baby-life", "baby distance", "repulsion"
    color = "green"
