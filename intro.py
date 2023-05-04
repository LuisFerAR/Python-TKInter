from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')


l1 = Label(root, text='Hola mundo, mi primera etiqueta')
l2 = Label(root, text='Chao  mundo, segunda')
l3 = Label(root, text='     dasdasdas                       ')

#label = Label(root, text='Hola mundo, mi primera etiqueta')
#label.pack()
#Label(root, text='Hola mundo! mi primera etiqueta').pack() OTRA FORMA
l1.grid(row=0, column=0)
l3.grid(row=1, column=1)
l2.grid(row=10, column=10)



root.mainloop()

