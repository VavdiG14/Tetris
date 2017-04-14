#tabela kock in njihovih rotacoj
kocke = {"levil": [(-1, 0), (0, 0), (0, -1), (0, -2)], "desnil": [(0, 0), (1, 0), (0, -1), (0, -2)],
         "kvadrat": [(0, 0), (0, 1), (-1, 0), (-1, 1)], "kockat": [(0, 0), (-1, 0), (1, 0), (0, -1)],
         "palcka": [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
         "leviz": [(-1, -1), (0, -1), (0, 0), (1,0)], "desniz": [(1, -1), (0, -1), (0, 0), (-1,0)]}

class Kocka():
    def __init__(self,vrsta):
        self.vrsta=vrsta
        self.koordnidate=kocke[vrsta]

    def __str__(self):
        return self.vrsta

    def rotacijavdesno(self):
        nove_koordnate=[]
        for tocke in self.koordnidate:
            x=tocke[0]
            y=tocke[1]
            nove_koordnate.append((-y,x))
        self.koordnidate=nove_koordnate

    def rotacijavlevo(self):
        nove_koordnate = []
        for tocke in self.koordnidate:
            x = tocke[0]
            y = tocke[1]
            nove_koordnate.append((y, -x))
        self.koordnidate = nove_koordnate

