###Uvod v programiranje igrice Tetris

from tkinter import*
from tabelakock import kocka
import time
#definiramo širino kvadratka, ki nam bo služil kot merilo za velikost elementov.
k = 30
zacetekx=k*15/2
zaceteky=0
kocke = {"levil": [(-1, 0), (0, 0), (0, -1), (0, -2)], "desnil": [(0, 0), (1, 0), (0, -1), (0, -2)],
         "kvadrat": [(0, 0), (0, 1), (-1, 0), (-1, 1)], "kockat": [(0, 0), (-1, 0), (1, 0), (0, -1)],
         "palcka": [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
         "leviz": [(-1, -1), (0, -1), (0, 0), (1, 0)], "desniz": [(1, -1), (0, -1), (0, 0), (-1, 0)]}
vse_kocke=kocke.keys()
class GUI():

    def __init__(self, master):
        self.platno = Canvas(master, width=15*k, height=20*k, background='black')
        self.platno.pack(side=RIGHT)
        menu = Menu(master)
        master.config(menu=menu)
        f = Frame(master)
        f.pack()
        GUI.risanjekock(self, "kvadrat")
        GUI.padanje_kocke(self, 3)


    def risanjekock(self,vrstakocke):
        koord= kocka(vrstakocke).koordnidate
        kor1=list(map(lambda x: x * k, koord[0]))
        kor2=list(map(lambda x: x * k, koord[1]))
        kor3=list(map(lambda x: x * k, koord[2]))
        kor4=list(map(lambda x: x * k, koord[3]))
        self.koc1 = self.platno.create_rectangle(zacetekx + kor1[0], zaceteky + kor1[1], zacetekx + kor1[0] + k,zaceteky + kor1[1] + k, fill = 'pink')
        self.koc2 = self.platno.create_rectangle(zacetekx + kor2[0], zaceteky + kor2[1], zacetekx + kor2[0] + k,zaceteky + kor2[1] + k, fill = 'pink')
        self.koc3 = self.platno.create_rectangle(zacetekx + kor3[0], zaceteky + kor3[1], zacetekx + kor3[0] + k,zaceteky + kor3[1] + k, fill = 'pink')
        self.koc4 = self.platno.create_rectangle(zacetekx + kor4[0], zaceteky + kor4[1], zacetekx + kor4[0] + k,zaceteky + kor4[1] + k, fill = 'pink')
        self.platno.update()
    def padanje_kocke(self,level):
        t=18
        while t:
            self.platno.after(1000)
            self.platno.move(self.koc1, 0, k)
            self.platno.move(self.koc2, 0, k)
            self.platno.move(self.koc3, 0, k)
            self.platno.move(self.koc4, 0, k)
            self.platno.update()
            t-=1
    def premikvlevo(self):
        self.platno.move(self.koc1, -k, 0)
        self.platno.move(self.koc2, -k, 0)
        self.platno.move(self.koc3, -k, 0)
        self.platno.move(self.koc4, -k, 0)
        self.platno.update()
    def premikvdesno(self):
        self.platno.move(self.koc1, k, 0)
        self.platno.move(self.koc2, k, 0)
        self.platno.move(self.koc3, k, 0)
        self.platno.move(self.koc4, k, 0)
        self.platno.update()








root = Tk()
app=GUI(root)
root.mainloop()
