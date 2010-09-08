#!/usr/bin/env python3.1
import sys
import tkinter as tk

def main():
	root = tk.Tk()
	root.title("This Thing")
	root.geometry("600x400")
	
	circle = tk.PhotoImage(file="circle.gif") # gif is only natively supported format
	
	circle_control = tk.Label(root, image=circle)
	circle_control.place(x=20, y=20)
	circle_control.place(x=100, y=20)
	
	print(dir(circle_control))
	
	x = 0
	def tick():
		nonlocal x # necessary to assign to a variable outside of this function
		
		x = x + 5
		if x > 600:
			# wrap around
			x = -92
		
		circle_control.place(x=x)
		
		root.after(50, tick)
	
	root.after(50, tick)
	root.mainloop()

if __name__ == "__main__":
	sys.exit(main(*sys.argv[1:]))
