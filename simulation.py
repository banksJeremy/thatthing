#!/usr/bin/env python3.1
from random import random, randint

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
        
        # we're randomly changing the attributes of each thing as a demo.
        
        for thing in self.things:
            thing.x = thing.x + randint(-1, 1)
            thing.y = thing.y + randint(-1, 1)
            thing.radius = thing.radius + randint(-1, 1)

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









def main():
    "Set up and display a simple simulation when this file is run."
    
    from display import display_and_run
    
    world = World(512, 512)
    world.populate(10 * [Animal] + 5 * [Plant])
    display_and_run(world, frequency=60)

if __name__ == "__main__":
    import sys
    sys.exit(main(*sys.argv[1:]))
