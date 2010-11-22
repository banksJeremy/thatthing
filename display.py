#!/usr/bin/env python3.1
import simulation
import tkinter as tk
from collections import namedtuple
from itertools import zip_longest

def display_and_run(world):
    root = tk.Tk("Foo")
    canvas = tk.Canvas(root, width=world.width, height=world.height)
    canvas.pack()
    
    def draw_thing(thing):
        return canvas.create_oval(
            thing.x - thing.radius, thing.y - thing.radius,
            thing.x + thing.radius, thing.y + thing.radius,
            width=2, fill=thing.color)
    
    sprites = list(map(draw_thing, world.things))
    
    try:
        while True:
            root.update_idletasks()
            root.update()
        
            for sprite, thing in list(zip_longest(sprites, world.things, fillvalue="EOL")):
                if sprite == "EOL":
                    sprite = draw_thing(thing)
                    sprites.append(sprite)
                    continue
                
                if thing == "EOL":
                    canvas.delete(sprite)
                    sprites.pop()
                    continue
                
                canvas.coords(sprite,
                              thing.x - thing.radius, thing.y - thing.radius,
                              thing.x + thing.radius, thing.y + thing.radius)
                canvas.itemconfigure(sprite, fill=thing.color)
        
            old_things = world.things
            world.tick()
    except tk.TclError as ex:
        print("Termination error:", ex)

def main():
    world = simulation.World(512, 512)
    world.populate(10 * [simulation.Animal] + 5 * [simulation.Plant])
    display_and_run(world)

if __name__ == "__main__":
    import sys
    sys.exit(main(*sys.argv[1:]))
