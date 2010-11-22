#!/usr/bin/env python3.1
import simulation
import tkinter as tk
from collections import namedtuple

def display_and_run(world):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=world.width, height=world.height)
    canvas.pack()
    
    def draw_thing(thing):
        return canvas.create_oval(
            thing.x - thing.radius, thing.y - thing.radius,
            thing.x + thing.radius, thing.y + thing.radius,
            width=2, fill=getattr(thing, "color", "black"))
    
    sprites = list(map(draw_thing, world.things))
    
    while True:
        root.update_idletasks()
        root.update()
        
        for sprite, thing in zip(sprites, world.things):
            canvas.coords(sprite,
                          thing.x - thing.radius, thing.y - thing.radius,
                          thing.x + thing.radius, thing.y + thing.radius)
        
        old_things = world.things
        world.tick()

def main():
    world = simulation.World(512, 512)
    world.populate(10 * [simulation.Animal] + 5 * [simulation.Plant])
    display_and_run(world)

if __name__ == "__main__":
    import sys
    
    sys.exit(main(*sys.argv[1:]))
