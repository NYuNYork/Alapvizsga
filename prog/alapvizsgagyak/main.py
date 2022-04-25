import modul as m
from cmath import sqrt
import math

# #1.feladat
# szam = int(input('addj meg egy számot:  '))
# szo = input('addj meg egy szót: ')
# b = szo + " "
# print(szam*b)

# #2.feladat
# a = float(input('add meg az a oldalt:   '))
# b = float(input('add meg a b oldalt:    '))
# c = float(input('add meg a c oldalt:    '))
# if a + b > c and a + c > b and b + c > a:
#     print('képezhető 3szög')
#     if a == b or a == c or b == c:
#         print('egynlőszárú')
#     if (a*a + b*b) == c*c or (a*a + c*c) == b*b or (b*b + c*c) == a*a:
#         print('derékszögű')
#     k = a + b + c
#     s = k / 2
#     t = sqrt(s*(s-a)*(s-b)*(s-c))
#     print(k)
#     print(t)
# else:
#     print('nem képezhető')

#3.feladat

f = open('D:/prog/alapvizsgagyak/solsys.txt','r', encoding='utf=8')

lista = []

for sor in f:
    vagott = sor.strip().split(';')
    lista.append(m.Bolygok(vagott[0],vagott[1],vagott[2]))
print(vagott[1])
print(len(lista))

