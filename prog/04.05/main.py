import modul3 as m

f = open('D:/prog/04.05/employes.txt','r', encoding='utf=8')

lista = []

for sor in f:
    vagott = sor.strip().split(';')
    lista.append(m.Osztaly(vagott[0],vagott[1].strip('$'),vagott[2],vagott[3]))

print(len(lista))