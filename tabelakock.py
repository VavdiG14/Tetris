#tabela kock in njihovih rotacij
kocke = {"levil": [[(-1, 1), (0, 0), (0, -1), (0, 1)], [(-1, -1), (0, 0), (1, 0), (-1, 0)], [(1, -1), (0, 0), (0, 1), (0, -1)], [(1, 1), (0, 0), (-1, 0), (1, 0)]],
         "desnil": [[(0, 0), (1, 1), (0, -1), (0, 1)], [(0, 0), (-1, 1), (1, 0), (-1, 0)], [(0, 0), (-1, -1), (0, 1), (0, -1)], [(0, 0), (1, -1), (-1, 0), (1, 0)]],
         "kvadrat": [[(0, 0), (0, 1), (-1, 0), (-1, 1)]],
         "kockat": [[(0, 0), (-1, 0), (1, 0), (0, -1)], [(0, 0), (0, -1), (0, 1), (1, 0)], [(0, 0), (1, 0), (-1, 0), (0, 1)], [(0, 0), (0, 1), (0, -1), (-1, 0)]],
         "palcka": [[(1, 0), (0, 0), (-1, 0), (-2, 0)],[(0, 1), (0, 0), (0, -1), (0, -2)]],
         "leviz": [[(-1, -1), (0, -1), (0, 0), (1, 0)], [(1, -1), (1, 0), (0, 0), (0, 1)], [(1, 1), (0, 1), (0, 0), (-1, 0)], [(-1, 1), (-1, 0), (0, 0), (0, -1)]],
         "desniz": [[(1, -1), (0, -1), (0, 0), (-1, 0)], [(1, 1), (1, 0), (0, 0), (0, -1)], [(-1, 1), (0, 1), (0, 0), (1, 0)], [(-1, -1), (-1, 0), (0, 0), (0, 1)]]}

class Lik():
    def __init__(self,vrsta):
        self.vrsta=vrsta
        self.koordnidate=kocke[vrsta]

    def __str__(self):
        return self.vrsta


    def rotacijavlevo(self):
        nove_koordnate = []
        for tocke in self.koordnidate:
            x = tocke[0]
            y = tocke[1]
            nove_koordnate.append((y, -x))
        self.koordnidate = nove_koordnate

def rotacijavdesno(koor):
        nove_koordnate=[]
        for tocke in koor:
            x=tocke[0]
            y=tocke[1]
            nove_koordnate.append((-y,x))
        return nove_koordnate
def napisivserotac(sez):
    mnozica=[]
    prva=sez[0]
    mnozica.append(prva)
    nove = rotacijavdesno(prva)
    for i in range(5):
        if nove not in mnozica:
            mnozica.append(nove)
        nove=rotacijavdesno(nove)
    return list(mnozica)

print(napisivserotac([[(1, -1), (0, -1), (0, 0), (-1,0)]]))
