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

class Objekt():
    '''V nadaljevanju naj bi bil to class Objekt s katerim bi
     premikali in
    rotirali dani objekt..'''

    def __init__(self, igrica,vrsta):
        self.dno = dno
        self.igrica = igrica
        self.risanjeKock(vrsta)
        self.padanje_kocke()
        self.igrica.platno.update()
        self.igrica.platno.bind("<Left>", self.premikvLevo)
        self.igrica.platno.bind("<Right>", self.premikvDesno)


    def risanjeKock(self,vrstakocke):
        '''Izriše Objekt na platno.'''
        koord= Kocka(vrstakocke).koordnidate
        kor1=list(map(lambda x: x * k, koord[0]))
        kor2=list(map(lambda x: x * k, koord[1]))
        kor3=list(map(lambda x: x * k, koord[2]))
        kor4=list(map(lambda x: x * k, koord[3]))
        self.koc1 = self.igrica.platno.create_rectangle(zacetekx + kor1[0], zaceteky + kor1[1], zacetekx + kor1[0] + k,zaceteky + kor1[1] + k, fill = 'pink')
        self.koc2 = self.igrica.platno.create_rectangle(zacetekx + kor2[0], zaceteky + kor2[1], zacetekx + kor2[0] + k,zaceteky + kor2[1] + k, fill = 'pink')
        self.koc3 = self.igrica.platno.create_rectangle(zacetekx + kor3[0], zaceteky + kor3[1], zacetekx + kor3[0] + k,zaceteky + kor3[1] + k, fill = 'pink')
        self.koc4 = self.igrica.platno.create_rectangle(zacetekx + kor4[0], zaceteky + kor4[1], zacetekx + kor4[0] + k,zaceteky + kor4[1] + k, fill = 'pink')
        self.igrica.platno.update()

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
        self.kocka = Objekt(self,'palcka')






root = Tk()
app=GUI(root)
root.mainloop()
