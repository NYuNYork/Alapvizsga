import modul as m
f = open('legmagasabb.txt','r', encoding='utf=8')

lista =[]

for sor in f:
    vagott = sor.strip().split(';')
    lista.append(m.Kategoria(vagott[0],vagott[1],vagott[2],vagott[3],vagott[4],vagott[5]))

print(f'2.feladat {len(lista)}db')


osszemelet = 0

for e in lista:
    osszemelet += e.emelet
print(f'emeletek összege:{osszemelet}')

maxi = 0 
for i in range(1, len(lista)):
    if lista [i].magassag > lista[maxi].magassag:
        maxi = i
        print (lista[maxi].nev,lista[maxi].varos,lista[maxi].orszag,lista[maxi].magassag,lista[maxi].emelet,lista[maxi].epult) 

for c in lista:
    if c.orszag in 'Olaszország':
        print('van olasz épület')
    