from cmath import sqrt

def elsofeladat():
    szoveg = input('addj meg egy szót: ')
    szam = int(input('addj meg egy számot: '))
    print((szam*szam)*szoveg.lower())


def masodikfel():
    a = float(input('Add meg az a oldalt: '))
    b = float(input('Add meg a b oldalt: '))
    c = float(input('Add meg a c oldalt: '))
    if a + b > c and a + c > b and b + c > a:
        print('képezhető')
    if a == b or a == c or b == c:
        print('egyenlőszárú')
    if (a*a) + (b*b) == c*c or (a*a) + (c*c) == b*b or (b*b) + (c*c) == a*a:
        print('derékszögű')
    k = a + b + c
    s = k / 2
    t = sqrt(s*(s-a)*(s-b)*(s-c))
    print(f'területe:{t}')
    print(f'kerülete:{k}')


class Bolygo:
    def __init__(self,r:str):
        v = r.strip().split(';')
        self.nev:str = v[0]
        self.holdak_szama:int = int(v[1])
        self.terfogat_arany:float = float(v[2])

def f3_0(f:str, e:str):
    bs:list[Bolygo] = []
    for r in open(file=f, encoding=e):
        bs.append(Bolygo(r))
    return bs


def f3_2(bs:list[Bolygo]):
    sum = 0
    for b in bs:
        sum += b.holdak_szama
    print(sum / len(bs))

def f3_3(bs:list[Bolygo]):
    maxi = 0 
    for i in range(1, len(bs)):
        if bs[i].terfogat_arany > bs[maxi].terfogat_arany:
            maxi = i
    return bs[maxi].nev

def f3_4(bs:list[Bolygo]):
    n = input('addj meg a keresett bolygót:')
    x = 0
    for b in bs:
        if n in b.nev:
            x += 1
    if x == 0: print('Nincs ilyen bolygó')
    if x > 0: print('Van ilyen bolygó')