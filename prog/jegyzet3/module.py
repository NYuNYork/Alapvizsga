from math import sqrt

def elso_feladat() -> None:
    n:int = pow(int(input('\tÍrj be egy számot: ')), 2)
    s:str = input('\tÍrj be egy szöveget: ').lower() + ' '
    print(f'\tOP: {n * s}')


def masodik_feladat() -> None:
    a:float = float('\tAdd meg az [a] értékét: ')
    b:float = float('\tAdd meg az [b] értékét: ')
    c:float = float('\tAdd meg az [c] értékét: ')
    if a+b>c and a+c>b and b+c>a:
        print('\tLétezhet háromszög ilyen oldalhosszakkal')
        if a==b or a==c or b==c:
            print('\tA háromszög egyenlő szárú')
        else:
            print('\tA háromszög NEM egyenlő szárú')
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print('\tA háromszög derékszögű')
        else:
            print('\tA háromszög NEM derékszögű')
        k = a + b + c
        print(f'\tA háromszög kerülete: {k} cm')
        s = k / 2
        t = sqrt(s*(s-a)*(s-b)*(s-c))
        print(f'\tA háromszög területe: {t} cm^2')
    else:
        print('\tNEM létezhet ilyen háromszög')


class Bolygo:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.holdak_szama:int = int(v[1])
        self.terfogat_arany:float = float(v[2])


def get_bolygok(f:str, e:str) -> list[Bolygo]:
    bolygok:list[Bolygo] = []
    for sor in open(file=f, encoding=e):
        bolygok.append(Bolygo(sor))
    return bolygok


def holak_atlagos_szama(bolygok:list[Bolygo]) -> float:
    holdak_szama_osszesen = 0
    for b in bolygok:
        holdak_szama_osszesen += b.holdak_szama
    return holdak_szama_osszesen / len(bolygok)


def legnagyobb_terfogatu_bolygo(bolygok:list[Bolygo]) -> str:
    maxi = 0
    for i in range(1, len(bolygok)):
        if bolygok[i].terfogat_arany > bolygok[maxi].terfogat_arany:
            maxi = i
    return bolygok[maxi].nev


def bolygo_kereses(keresett_bolygo_neve:str, bolygok:list[Bolygo]) -> bool:
    for b in bolygok:
        if b.nev.lower() == keresett_bolygo_neve.lower():
            return True
    return False


def tobb_holdja_van_mint(feltetel:int, bolygok:list[Bolygo]) -> list[str]:
    megfelelo_nevek:list[str] = []
    for b in bolygok:
        if b.holdak_szama > feltetel:
            megfelelo_nevek.append(b.nev)
    return megfelelo_nevek





