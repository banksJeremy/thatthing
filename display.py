#!/usr/bin/env python3.1
import simulation
import tkinter as tk
from collections import namedtuple
from itertools import zip_longest
from time import time, sleep

def display_and_run(world, frequency, title="Simulation Display"):
    root = tk.Tk()
    root.title(title)
    canvas = tk.Canvas(root, width=world.width, height=world.height)
    canvas.pack()
    
    def draw_thing(thing):
        return canvas.create_oval(
            thing.x - thing.radius, thing.y - thing.radius,
            thing.x + thing.radius, thing.y + thing.radius,
            width=2, fill=thing.color)
    
    sprites = list(map(draw_thing, world.things))
    last_time = time()
    interval = 1 / frequency
    
    try:
        while True:
            root.update_idletasks()
            root.update()
            
            new_sprites = []
            
            for sprite, thing in zip_longest(sprites, world.things, fillvalue="EOL"):
                if sprite == "EOL":
                    sprite = draw_thing(thing)
                    new_sprites.append(sprite)
                    continue
                
                if thing == "EOL":
                    canvas.delete(sprite)
                    continue
                
                new_sprites.append(sprite)
                
                canvas.coords(sprite,
                              thing.x - thing.radius, thing.y - thing.radius,
                              thing.x + thing.radius, thing.y + thing.radius)
                canvas.itemconfigure(sprite, fill=thing.color)
            
            sprites = new_sprites
            old_things = world.things
            
            outstanding_time = last_time - time() + interval
            
            if outstanding_time > 0:
                sleep(outstanding_time)
            
            world.tick()
            
            last_time = time()
    except tk.TclError as ex:
        print("Termination error:", ex)
