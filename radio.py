from tkinter import *

root = Tk()
root.title('Hola mundo')

r = IntVar()
r.set('2')

# Radiobutton(root, text='Opcion 1', variable=r, value=1).pack()
# Radiobutton(root, text='Opcion 2', variable=r, value=2).pack()
# l = Label(root, textvariable=r)


CHANCHITOS =[
    ('Feliz', 'Feliz'),
    ('Triste', 'Triste'),
    ('Amargado', 'Amargado'),
    ('Wolfgang', 'Wolfgang')
]

chanchito = StringVar()
chanchito.set('lala')

for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()

l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()