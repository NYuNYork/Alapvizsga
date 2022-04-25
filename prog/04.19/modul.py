class Osztaly:
    def __init__(self, r:str):
        v = r.strip().split(';')
        self.nev:str = v[0]
        self.fizu:int = int(v[1].strip('$'))
        self.szul_ev:int = int(v[2])
        self.szekhely:str = v[3]
        

def f3_0(f:str, e:str):
    bs:list[Osztaly] = []
    for r in open(file=f, encoding=e):
        bs.append(Osztaly(r))
    return bs

def atlagfizu(bs:list[Osztaly]):
    sum = 0
    for b in bs:
        sum += b.fizu
    return sum / len(bs)

def kereso(bs:list[Osztaly]):
    n = input('addj meg egy nevet')
    for b in bs:
        if n in b.nev:
            print(b.fizu,b.szul_ev,b.szekhely)
    else: print('nincs ilyen nevű alkalmazott')