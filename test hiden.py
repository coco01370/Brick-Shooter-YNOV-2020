from tkinter import *
#function
def show():
    canvas1.pack()

def hide():
    canvas1.pack_forget()
#def
fenetre = Tk()
fenetre.geometry("500x270")
#button
show_button = Button(fenetre, text="show", command=show)
hide_button = Button(fenetre, text="hide", command=hide)
#fenetre
canvas1 = Canvas(fenetre, background="black")

#boutons.apparition
show_button.pack(side="left")
hide_button.pack(side="right")
#boucle
fenetre.mainloop()
