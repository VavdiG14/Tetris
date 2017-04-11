###Uvod v programiranje igrice Tetris

from tkinter import*

#definiramo širino kvadratka, ki nam bo služil kot merilo za velikost elementov.
k = 20

class GUI():

    def __init__(self, master):
        self.platno = Canvas(master, width=15*k, height=20*k, background='black')
        self.platno.pack(side=RIGHT)
        menu = Menu(master)
        master.config(menu=menu)
        f = Frame(master)
        f.pack()
        pravokotnik = self.platno.create_rectangle(100,100, 100+k, 200-k, fill = 'blue')
        pravokotnik_r1 = self.platno.create_rectangle(150, 100, 150-k, 100+k, fill='green')







root = Tk()
app=GUI(root)
root.mainloop()
