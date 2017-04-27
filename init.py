###Uvod v programiranje igrice Tetris
# -*- coding: "utf-8" -*-

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
    '''Razreed v katerem rišemo like, jih premikamo in rotiramo..'''

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
        self.igrica.platno.bind("<space>", self.rotiranjeLika)
        self.igrica.platno.bind("<Up>",self.rotiranjeLika)
        self.igrica.platno.bind("<Down>", self.hitrejeDol)
        self.padanjeLika()

    def narisiLik(self):
        '''Metoda izriše trenutni lik'''
        if self.koord[0][7] is not None:
                result = messagebox.askquestion("Konec igre", "Želite igrati ponovno?", icon='warning')
                if result == 'no':
                    self.igrica.koncajIgro()
                else:
                    self.igrica.ponovnaIgra()
        else:
            for (u,v) in self.oblika[self.rotacija % len(self.oblika)]:
                id = self.igrica.platno.create_rectangle(
                    self.x * k +(u * k), self.y*k +(v*k), self.x*k +(u+1)*k, self.y* k + (v+1) * k, fill = self.barva)
                self.gids.append(id)
            self.igrica.platno.update()



    def rotiranjeLika(self, events):
        '''Rotiranje lika v smeri urinega kazalca'''
        oren = (self.rotacija + 1 )% len(self.oblika)
        if self.preveriPremik(oren, self.x, self.y):
            self.rotacija = oren
            i = 0
            for (u, v) in self.oblika[oren]:
                    self.igrica.platno.coords(self.gids[i], self.x*k +(u * k), self.y*k +(v*k), self.x*k +(u+1)*k,
                                              self.y*k + (v+1) * k)
                    i += 1
            self.igrica.platno.update()

    def padanjeLika(self):
        '''Lik se spušča proti dnu'''
        tabeleaHitrosti = [700, 600, 500, 400, 350, 300, 250, 225, 200, 190, 180, 170, 160, 150, 140, 130, 120,
                110, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
        hitrost=tabeleaHitrosti[self.igrica.level]
        if self.preveriPremik(self.rotacija, self.x, self.y+1):
            self.igrica.platno.update()
            for i in self.gids:
                self.igrica.platno.move(i, 0, k)
            self.y += 1
            self.igrica.platno.after(hitrost, self.padanjeLika)
        else:
            self.osveziTabelo(self.rotacija, self.x, self.y)
            self.igrica.naslednjiLik(self.koord)

    def hitrejeDol(self,event):
        if self.preveriPremik(self.rotacija, self.x, self.y+1):
            self.igrica.platno.update()
            for i in self.gids:
                self.igrica.platno.move(i, 0, k)
            self.y += 1
        else:
            self.osveziTabelo(self.rotacija, self.x, self.y)


    def premikvLevo(self,event):
        '''Premikanje lika v levo'''
        if self.preveriPremik(self.rotacija, self.x -1, self.y):
            for u in self.gids:
                self.igrica.platno.move(u, -k, 0)
            self.x -= 1
        self.igrica.platno.update()


    def premikvDesno(self,event):
        '''Premikanje lika v desno'''
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
        print(self.koord)
        i = 0
        for (u, v) in self.oblika[orientacija]:
            novX = u + x
            novY = v + y
            (self.koord[novY])[novX] = self.gids[i]
            i += 1
        vrstice=[]
        for st,vrstica in enumerate(self.koord):
            if None not in vrstica:
                for gid in vrstica:
                    self.igrica.platno.delete(gid)
                for st2 in range(st+1):
                    for gid in self.koord[st2]:
                            if gid is not None:
                                self.igrica.platno.move(gid, 0, k)
                vrstice.append(vrstica)
        for vrst in vrstice:
            self.koord.remove(vrst)
            self.koord = [[None for i in range(15)]] + self.koord
            self.igrica.tocke+=1
            if self.igrica.tocke>0 and self.igrica.tocke%5==0:
                self.igrica.level+=1
        self.igrica.platno.itemconfigure(self.igrica.tekstlevel, text= "Level: "+str(self.igrica.level))
        self.igrica.platno.itemconfigure(self.igrica.teksttocke, text= "Tocke: "+str(self.igrica.tocke))




class GUI():
    '''Tukaj je definiran uporabniški vmesnik'''

    def __init__(self, master):
        self.platno = Canvas(master, width=15*k, height=20*k, background='black')
        self.platno.pack(side=RIGHT)
        self.tocke=0
        self.level=1
        menu = Menu(master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title('Tetris')
        master.config(menu=menu)
        menu.add_command(label="Nova igra", command=self.novaIgra)
        menu.add_command(label="Koncaj", command=self.koncajIgro)
        menu.add_command(label="Navodila", command=self.navodila)
        self.platno.focus_set()
        self.igra = False



    def naslednjiLik(self,koord=[[None for i in range(15)] for j in range(20)]):
        barve = ['green', 'blue', 'red', 'pink',"yellow","purple","orange","violet",'cyan','aqua','palegreen']
        nakljucnaBarva = random.choice(barve)
        return Lik(self, random.choice(vse_kocke), nakljucnaBarva,koord,)

    def novaIgra(self):
        if self.igra:
            messagebox.Message("Igra je v teku")

        else:
            self.platno.delete(ALL)
            self.tocke = 0
            self.level = 1
            self.igra = not self.igra
            self.teksttocke=self.platno.create_text(k*1+40,20, font=('Helvetica',24,'bold'), text=("Tocke: 0").encode('utf8'), fill="White")
            self.tekstlevel=self.platno.create_text(k*15-70, 20,font=('Helvetica',24,'bold'),text="level: 1",fill="white" )
            self.kocka = self.naslednjiLik([[None for i in range(15)] for j in range(20)])

    def ponovnaIgra(self):
        '''TODO:napiši konec igre'''
        self.igra = False
        self.novaIgra()

    def koncajIgro(self):
        result = messagebox.askquestion("Končaj igro", "Želite končati igro?", icon='warning')
        if result == 'yes':
            self.master.destroy()

    def navodila(self):
        okno = Toplevel()
        okno.minsize(width=200, height=250)
        okno.title('Navodila')
        #okno.resizable(width=False, height=False)
        canvas = Canvas(okno, width=806, height=537)
        canvas.pack()
        canvas.focus_set()
        img = PhotoImage(file='navodila.gif')
        canvas.create_image(806, 537, image=img)

root = Tk()
app=GUI(root)
root.mainloop()