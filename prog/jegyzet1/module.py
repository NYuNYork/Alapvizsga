class Eredmeny:
    def __init__(self, r):
        v = r.strip().split(' ')
        self.helyezes = int(v[0])
        self.sportolok = int(v[1])
        self.sportag = v[2]
        self.versenyszam = v[3]
        # ternary operator
        self.pontszam = 7 if self.helyezes == 1 else 7 - self.helyezes


def get_eredmenyek(f):
    lst = []
    for s in open(f):
        lst.append(Eredmeny(s))
    return lst


def get_ermek(lst):
    a = 0
    e = 0
    b = 0
    for x in lst:
        if x.helyezes == 1: a += 1
        elif x.helyezes == 2: e += 1
        elif x.helyezes == 3: b += 1
    print(f'arany: {a}')
    print(f'ezüst: {e}')
    print(f'bronz: {b}')
    print(f'összesen: {a + e + b}')


def get_pontszamok_osszege(lst):
    sum = 0
    for x in lst:
        sum += x.pontszam
    return sum


def create_helsinkitxt2(lst):
    helsinki2 = open("helsinki2.txt", "w")
    for x in lst:
        sprtg = x.sportag if x.sportag != 'kajakkenu' else 'kajak-kenu'
        helsinki2.write(f'{x.helyezes} {x.sportolok} {x.pontszam} {sprtg} {x.versenyszam}\n')
    helsinki2.close()


def get_tobberem(lst, sn1, sn2):
    s1e = 0
    s2e = 0
    for x in lst:
        if x.helyezes in [1, 2, 3]:
            if x.sportag == sn1:
                s1e += 1
            if x.sportag == sn2:
                s2e += 1
    if s1e > s2e:
        print(f'{sn1}-ban/ben szereztek több érmet')
    elif s2e > s1e:
        print(f'{sn2}-ban/ben szereztek több érmet')
    else:
        print(f'{sn1} és {sn2} sportágakban az érmek száma egyenlő volt')


def get_max_sportolo_szam(lst):
    maxi = 0
    for i in range(1, len(lst)):
        if lst[i].sportolok > lst[maxi].sportolok:
            maxi = i
    return lst[maxi]