###Uvod v programiranje igrice Tetris

from tkinter import*
from tabelakock import*
import random
from tkinter import messagebox

#definiramo širino kvadratka, ki nam bo služil kot merilo za velikost elementov.
k = 30
zacetekx=7
zaceteky=0
dno = 17
vse_kocke=list(kocke.keys())

class Lik():
    '''V nadaljevanju naj bi bil to class Objekt s katerim bi
     premikali in
    rotirali dani objekt..'''

    def __init__(self, igrica,imeLika,barva,koord):
        self.barva = barva
        self.oblika = kocke[imeLika]#dobi seznam vseh oblik lika
        self.rotacija = 0   #privzeta trenutna rotacija
        self.x = zacetekx
        self.y = zaceteky
        self.koord = koord
        self.gids = []
        self.igrica = igrica
        self.narisiLik()
        self.igrica.platno.bind("<Left>", self.premikvLevo)
        self.igrica.platno.bind("<Right>", self.premikvDesno)
        self.igrica.platno.bind("<space>", self.rotiranje)
        self.padanje_kocke()

    def narisiLik(self):
        if self.koord[0][7] is not None:
            messagebox.showinfo("Koncaj igro", "This is a Test")
        else:
            for (u,v) in self.oblika[self.rotacija % len(self.oblika)]:
                id = self.igrica.platno.create_rectangle(
                    self.x * k +(u * k), self.y*k +(v*k), self.x*k +(u+1)*k, self.y* k + (v+1) * k, fill = self.barva)
                self.gids.append(id)



    def rotiranje(self, events):
        oren = (self.rotacija + 1 )% len(self.oblika)
        if self.preveriPremik(oren, self.x, self.y):
            self.rotacija = oren
            i = 0
            for (u, v) in self.oblika[oren]:
                    self.igrica.platno.coords(self.gids[i], self.x*k +(u * k), self.y*k +(v*k), self.x*k +(u+1)*k,
                                              self.y*k + (v+1) * k)
                    i += 1

    def padanje_kocke(self,level = 3):
        '''Kocka se spušča proti dnu'''
        self.igrica.platno.update()
        if self.preveriPremik(self.rotacija, self.x, self.y+1):
            for i in self.gids:
                self.igrica.platno.move(i, 0, k)
            self.y += 1
            self.igrica.platno.after(250, self.padanje_kocke)
        else:
            self.osveziTabelo(self.rotacija, self.x, self.y)
            self.igrica.naslednjiLik(self.koord)

    def premikvLevo(self,event):
        '''Premikanje Objekta v levo'''
        if self.preveriPremik(self.rotacija, self.x -1, self.y):
            for u in self.gids:
                self.igrica.platno.move(u, -k, 0)
            self.x -= 1
        self.igrica.platno.update()

    def premikvDesno(self,event):
        '''Premikanje Objekta v desno'''
        if self.preveriPremik(self.rotacija, self.x+1, self.y):
            for u in self.gids:
                self.igrica.platno.move(u, k, 0)
            self.x += 1

        self.igrica.platno.update()

    def preveriPremik(self,orientacija, x,y):
        '''Metoda preveri ali je premik/rotacija dovoljena.
            Metoda vrača True/False'''
        for (u,v) in self.oblika[orientacija]:
            noviX = u + x
            noviY = v + y
            if noviY >= 20:     #če pade na tla
                return False
            if noviX < 0 or noviX >= 15:        #če se zaleti levo ali desno
                return False
            if self.koord[noviY][noviX] is not None:

                return False
        return True

    def osveziTabelo(self,orientacija, x,y):
        i = 0
        for (u, v) in self.oblika[orientacija]:
            novX = u + x
            novY = v + y
            (self.koord[novY])[novX] = self.gids[i]
            i += 1
        for st,vrstica in enumerate(self.koord):
            if None not in vrstica:
                for gid in vrstica:
                    self.igrica.platno.delete(gid)
                for st2 in range(st+1):
                    for gid in self.koord[st2]:
                            if gid is not None:
                                self.igrica.platno.move(gid, 0, k)
                self.koord.remove(vrstica)
                self.koord = [[None for i in range(16)]]+ self.koord



class GUI():
    '''Tukaj bo definiran uporabniški vmesnik'''

    def __init__(self, master):
        self.platno = Canvas(master, width=15*k, height=20*k, background='black')
        self.platno.pack(side=RIGHT)
        menu = Menu(master)
        master.config(menu=menu)
        menu.add_command(label="Nova igra", command=self.novaIgra)
        menu.add_command(label="Koncaj", command=master.destroy)
        self.platno.focus_set()



    def naslednjiLik(self,koord=[[None for i in range(15)] for j in range(20)]):
        barve = ['green', 'blue', 'red', 'pink']
        nakljucnaBarva = random.choice(barve)
        return Lik(self, random.choice(vse_kocke), nakljucnaBarva,koord)

    def novaIgra(self):
        self.kocka = self.naslednjiLik()


root = Tk()
app=GUI(root)
root.mainloop()