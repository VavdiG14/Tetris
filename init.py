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
        self.oblika = [kocke[imeLika]]#dobi seznam vseh oblik lika
        self.rotacija = 0   #privzeta trenutna rotacija
        self.gids = []
        self.igrica = igrica
        self.narisiLik()
        self.igrica.platno.bind("<Left>", self.premikvLevo)
        self.igrica.platno.bind("<Right>", self.premikvDesno)
        self.igrica.platno.bind("<space>", self.rotiraj)

    def narisiLik(self):
        for (x,y) in self.oblika[self.rotacija%len(self.oblika)]:
            id = self.igrica.platno.create_rectangle(
                zacetekx +(x * k), zaceteky +(y*k), zacetekx +(x+1)*k, zaceteky + (y+1) * k, fill ='pink')
        self.gids.append(id)

    def osvezi(self):
        pass

    def rotiraj(self, events):
        self.rotacija += 1
        self.narisiLik()
        #Preveri, ali se ga da narisati, glede na druge postavitve
        self.osvezi()


    def padanje_kocke(self,level = 3):
        '''Kocka se spušča proti dnu'''
        self.igrica.platno.move(self.koc1, 0, k)
        self.igrica.platno.move(self.koc2, 0, k)
        self.igrica.platno.move(self.koc3, 0, k)
        self.igrica.platno.move(self.koc4, 0, k)
        #Tukaj bo moral gledati ali se je že zaletel v prejšno kocko/dno
        if self.dno == 0:
            print('Zdj se moreš ustavit')
            return 0
        else:
            self.dno -= 1
            self.igrica.platno.after(1000, self.padanje_kocke)


    def premikvLevo(self,event):
        '''Premikanje Objekta v levo'''
        #TODO: omeji njegovo gibanje glede na zaslon
        self.igrica.platno.move(self.koc1, -k, 0)
        self.igrica.platno.move(self.koc2, -k, 0)
        self.igrica.platno.move(self.koc3, -k, 0)
        self.igrica.platno.move(self.koc4, -k, 0)
        self.igrica.platno.update()

    def premikvDesno(self,event):
        '''Premikanje Objekta v desno'''
        #TODO: omeji njegovo gibanje glede na zaslon
        self.igrica.platno.move(self.koc1, k, 0)
        self.igrica.platno.move(self.koc2, k, 0)
        self.igrica.platno.move(self.koc3, k, 0)
        self.igrica.platno.move(self.koc4, k, 0)
        self.igrica.platno.update()



class GUI():
    '''Tukaj bo definiran uporabniški vmesnik'''

    def __init__(self, master):
        self.platno = Canvas(master, width=15*k, height=20*k, background='black')
        self.platno.pack(side=RIGHT)
        menu = Menu(master)
        master.config(menu=menu)
        self.platno.focus_set()
        self.kocka = Lik(self,'palcka')






root = Tk()
app=GUI(root)
root.mainloop()