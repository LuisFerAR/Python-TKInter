from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')

# def click():
#     messagebox.showwarning('Popup', 'hola mundo!')

# def click():
#     messagebox.showinfo('Popup', 'hola mundo!')

# def click():
#     messagebox.showerror('Popup', 'hola mundo :(!')


# def click():
#     respuesta=messagebox.askquestion('Popup', 'hola mundo :(!')
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'la respuesta fue '+respuesta)
#     else:
#         messagebox.showinfo('Respuesta', ':( la respuesta fue '+respuesta)

# def click():
#     respuesta = messagebox.askokcancel('Hola mundo', 'Desea realizar accion')
#     if respuesta:
#         messagebox.showinfo('hola mundo', 'La respuesta fue ok')
#     else:
#         messagebox.showinfo('hola mundo', 'La respuesta fue CANCELAR')

def click():
    respuesta = messagebox.askyesno('Hola mundo', 'Desea realizar accion')
    if respuesta:
        messagebox.showinfo('hola mundo', 'La respuesta fue yes')
    else:
        messagebox.showinfo('hola mundo', 'La respuesta fue no')

btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()