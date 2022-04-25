from module import create_helsinkitxt2, get_eredmenyek, get_ermek, get_max_sportolo_szam, get_pontszamok_osszege, get_tobberem

eredmenyek = get_eredmenyek('helsinki.txt')

print('3. feladat:')
print(f'pontszerző helyezések száma: {len(eredmenyek)}')
print('4. feladat:')
get_ermek(eredmenyek)
print('5. feladat:')
print(f'olimpiai pontok száma: {get_pontszamok_osszege(eredmenyek)}')
print('6. feladat:')
get_tobberem(eredmenyek, 'torna', 'uszas')
create_helsinkitxt2(eredmenyek)
print('8. feladat:')
rdmny = get_max_sportolo_szam(eredmenyek)
print(f'helyezés: {rdmny.helyezes}')
print(f'sportág: {rdmny.sportag}')
print(f'versenyszám: {rdmny.versenyszam}')
print(f'sportolók száma: {rdmny.sportolok}')


