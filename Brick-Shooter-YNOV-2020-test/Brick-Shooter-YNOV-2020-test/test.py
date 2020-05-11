from tkinter import *

def chargerImage(): 
    im=Image.open("noir .png") 
    photo = ImageTk.PhotoImage(im) 
    dicimg['fond'] = photo
    item = cadre.create_image(320,240,image =photo) 
    print("charger image")
    