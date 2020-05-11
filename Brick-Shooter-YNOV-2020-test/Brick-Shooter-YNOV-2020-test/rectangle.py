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


# self.canvas = Canvas(self, width=500, height=200, bd=0, highlightthickness=0)
#    self.canvas.create_rectangle(245,50,345,150, fill='white')
#
#   self.image = tk.PhotoImage(file='chess.png')
#  self.image_id = self.canvas.create_image(50,50, image=self.image)

#   self.canvas.move(self.image_id, 245, 100)

