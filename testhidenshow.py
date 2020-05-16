from tkinter import *
import time


fenetre = Tk()


def show ():
    blackbutton.pack()

def hiden ():
    blackbutton.pack_forget()
    


redbutton = Button(fenetre, text="Red", fg="red",command=show)
redbutton.pack( side = LEFT)

greenbutton = Button(fenetre, text="green", fg="green",command=hiden)
greenbutton.pack( side = LEFT )

bluebutton = Button(fenetre, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(fenetre, text="Black", fg="black")
blackbutton.pack( side = RIGHT)
blackbutton.configure(width=20, height=2, bg="#000033", fg="white")



fenetre.mainloop()