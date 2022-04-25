class Olimpia:
    def __init__(self,r:str):
        v = r.strip().split(' ')
        self.helyezes:int = int(v[0])
        self.szam:int = int(v[1])
        self.sportag_neve:str = v[2]
        self.versenyszam_neve:str = v[3]


def fajllbeillesztes(f:str, e:str):
    bs:list[Olimpia] = []
    for r in open(file=f, encoding=e):
        bs.append(Olimpia(r))
    return bs


def fel_4(bs:list[Olimpia]):
    arany = 0
    ezust = 0
    bronz = 0
    for b in bs:
        if b.helyezes == 1:
            arany += 1
        if b.helyezes == 2:
            ezust += 1
        if b.helyezes == 3:
            bronz += 1
    print(f'arany:{arany}')
    print(f'Ezüst{ezust}')
    print(f'Bronz:{bronz}')



def fel_5(bs:list[Olimpia]):
    pontok = 0
    x = 0
    y = 0
    for b in bs:
        if b.helyezes == 1:
            pontok += 7
        if b.helyezes == 2:
            pontok += 5
        if b.helyezes == 3:
            pontok += 4
        if b.helyezes == 4:
            pontok += 3
        if b.helyezes == 5:
            pontok += 2
        if b.helyezes == 6:
            pontok += 1
    print(f'Olimpiai pontok száma: {pontok}')

def fel_6(bs:list[Olimpia]):
    s1e = 0
    s2e = 0
    for x in bs:
        if x.helyezes in [1, 2, 3]:
            if x.sportag_neve == 'torna':
                s1e += 1
            if x.sportag_neve == 'uszas':
                s2e += 1
    if s1e > s2e:
        print(f'Tornában szereztek több érmet')
    elif s2e > s1e:
        print(f'Úszásban szereztek több érmet')
    else:
        print(f'tornában és úszásban sportágakban az érmek száma egyenlő volt')