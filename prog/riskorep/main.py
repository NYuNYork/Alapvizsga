
from textwrap import indent
import modul as m


f = open('titanic.txt','r', encoding='utf=8')

lista =[]

for sor in f:
    vagott = sor.strip().split(';')
    lista.append(m.Kategoria(vagott[0],vagott[1],vagott[2]))

print(f'2.feladat {len(lista)}db')


osszeg = 0
for i in lista:
    osszeg += i.tulelo + i.eltunt
    
print(f'3.feladat {osszeg}')    



kereses = input('4.feladat: Kulcsszó')

i = 0

while i < len(lista) and kereses.lower() not in lista[i].nev.lower():
    i += 1

if i < len(lista):
    print('van találat')

    for i in lista:
        if kereses.lower() in i.nev.lower():
            print(f'')

else:
    print('Nincs találat')




for i in lista:
    osszeg += i.tuleo +i.eltuntek 
    hatvan = osszeg * 0,60
    if hatvan < i.eltuntek:
        print(f'{i.nev}')
    


max = lista[0].tulelo
index = 0
for i in range(1,len(lista)):
    if lista[i].tuleo > max:
        max = lista[i].tulelo
        index = i
print(f'7.feladat {lista[nev]}')