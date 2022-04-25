from tkinter.tix import Tree


def keplet(ev):
    if ev % 400 == 0 or ev % 4 == 0 and ev % 100 != 0:
        return True
    else: 
        return False


def szokoev():
    ev1 = int(input('addjon meg egy évszámot: '))
    ev2 = int(input('addjon meg mégegy évszámot: '))

    szokoevek = []
    for ev in range(ev1,ev2 + 1):
        if keplet(ev):
            print(ev)
            szokoevek.append(ev)

    if len(szokoevek) == 0:
        print('nincs')