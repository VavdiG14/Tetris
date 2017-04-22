###Uvod v programiranje igrice Tetris

from tkinter import*
from tabelakock import*
import time
#definiramo širino kvadratka, ki nam bo služil kot merilo za velikost elementov.
k = 30
zacetekx=k*15/2
zaceteky=0
dno = 17
vse_kocke=kocke.keys()

class Lik():
    '''V nadaljevanju naj bi bil to class Objekt s katerim bi
     premikali in
    rotirali dani objekt..'''

    def __init__(self, igrica,imeLika):
        self.min_x = zacetekx
        self.max_x = zacetekx
        self.dno = dno
        self.oblika = kocke[imeLika]#dobi seznam vseh oblik lika
        self.rotacija = 1   #privzeta trenutna rotacija
        self.x = zacetekx
        self.y = zaceteky
        self.koord = []
        self.gids = []
        self.igrica = igrica
        self.narisiLik()
        self.igrica.platno.bind("<Left>", self.premikvLevo)
        self.igrica.platno.bind("<Right>", self.premikvDesno)
        self.igrica.platno.bind("<space>", self.rotiranje)
        self.padanje_kocke()

    def narisiLik(self):
        stevec = 0
        for (u,v) in self.oblika[self.rotacija % len(self.oblika)]:
            id = self.igrica.platno.create_rectangle(
                self.x +(u * k), self.y +(v*k), self.x +(u+1)*k, self.y + (v+1) * k, fill ='pink')
            self.koord.append([(self.x +(u * k), self.y +(v*k)), (self.x +(u+1)*k, self.y + (v+1) * k)])
            self.gids.append(id)


    def rotiranje(self, events):
        self.rotacija += 1
        r = []
        i  =0
        for (u, v) in self.oblika[self.rotacija % len(self.oblika)]:
                self.igrica.platno.coords(self.gids[i], self.x +(u * k), self.y +(v*k), self.x +(u+1)*k, self.y + (v+1) * k)
                r += [self.x +(u * k), self.x +(u+1)*k]
                self.koord[i] = [(self.x +(u * k), self.y +(v*k)), (self.x +(u+1)*k, self.y + (v+1) * k)]
                i+= 1
        self.min_x = min(r)
        self.max_x = max(r)
        print(self.min_x, self.max_x)
        #Tudi pri rotacijah moraš preveriti, ali se lahko sploh zarotira.
        #Preveri, ali se ga da narisati, glede na druge postavitve


    def padanje_kocke(self,level = 3):
        '''Kocka se spušča proti dnu'''
        self.igrica.platno.update()
        for i in self.gids:
            self.igrica.platno.move(i, 0, k)
        self.y += k

        self.igrica.platno.after(1000, self.padanje_kocke)


    def premikvLevo(self,event):
        '''Premikanje Objekta v levo'''
        self.min_x += -k
        if self.preveriPremik():
            for u in self.gids:
                self.igrica.platno.move(u, -k, 0)
            self.x -= k
            self.max_x += -k
        else:
            self.min_x += k

        self.igrica.platno.update()

    def premikvDesno(self,event):
        '''Premikanje Objekta v desno'''

        self.max_x += k
        print(self.min_x, self.max_x)
        if self.preveriPremik():
            for u in self.gids:
                self.igrica.platno.move(u, k, 0)
            self.x += k
            self.min_x += k
        else:
            self.max_x += -k

        self.igrica.platno.update()

    def preveriPremik(self):
        '''Metoda preveri ali je premik/rotacija dovoljena.
            Metoda vrača True/False'''
        #LEVO
        if self.min_x < 0:
            return False
        elif self.max_x > 15*k:
            return False
        else:
            return True

class GUI():
    '''Tukaj bo definiran uporabniški vmesnik'''

    def __init__(self, master):
        self.platno = Canvas(master, width=15*k, height=20*k, background='black')
        self.platno.pack(side=RIGHT)
        menu = Menu(master)
        master.config(menu=menu)
        self.platno.focus_set()
        self.kocka = Lik(self,'kockaT')






root = Tk()
app=GUI(root)
root.mainloop()