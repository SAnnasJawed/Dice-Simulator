import random
from tkinter import *

root = Tk()
root.title("Dice Simulator")
root.geometry("800x500")

label = Label(root, font=("times", 200))


def rollDice():
    num = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.config(text=f'{random.choice(num)}{random.choice(num)}')
    label.pack()


rollButton = Button(root, text="Lets roll..", bg='red', command=rollDice)
rollButton.place(x=380, y=400)

root.mainloop()
