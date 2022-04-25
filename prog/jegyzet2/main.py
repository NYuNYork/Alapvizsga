from module import Bolygo, bolygo_kereses, elso_feladat, get_bolygok, holak_atlagos_szama, legnagyobb_terfogatu_bolygo, masodik_feladat, tobb_holdja_van_mint

print('1. feladat:')
# elso_feladat()
print('2. feladat:')
# masodik_feladat()
print('3. feladat:')
bolygok:list[Bolygo] = get_bolygok('solsys.txt', 'utf-8')
print(f'\t3.1: {len(bolygok)} bolygó van a naprendszerben')
print(f'\t3.2: a naprendszerben egy bolygónak átlagosan {holak_atlagos_szama(bolygok)} holdja van')
print(f'\t3.3: a legnagyobb térfogatú bolygó a {legnagyobb_terfogatu_bolygo(bolygok)}')
keresett = input('\t3.4: írd be a keresett bolygó nevét: ')
if bolygo_kereses(keresett, bolygok):
    print('\t\tvan ilyen bolygó a naprendszerben')
else:
    print('\t\tsajnos nincs ilyen nevű bolygó a naprendszerben')
holdak_szama:int = int(input('\t3.5: írj be egy egész számot: '))
bolygo_nevek_listaja = tobb_holdja_van_mint(holdak_szama, bolygok)
print(f'\t\ta következő bolygóknak van {holdak_szama}-nál/nél több holdja:')
print(f'\t\t{bolygo_nevek_listaja}')