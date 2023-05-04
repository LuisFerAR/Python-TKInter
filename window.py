from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')


#SOLUCION 1
# def open():
#     img = ImageTk.PhotoImage(Image.open('images/2.jpg'))
#     top = Toplevel()
#     top.title('hola mundo, nueva ventana')
#     l = Label(top, text='Soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()
# btn = Button(root, text='Click', command=open).pack()

# root.mainloop()


# #SOLUCION 2
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('images/2.jpg'))
#     top = Toplevel()
#     top.title('hola mundo, nueva ventana')
#     l = Label(top, text='Soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
# btn = Button(root, text='Click', command=open).pack()

# root.mainloop()


#SOLUCION 3
def open(img):
    top = Toplevel()
    top.title('hola mundo, nueva ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()

img = ImageTk.PhotoImage(Image.open('images/2.jpg'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()

root.mainloop()