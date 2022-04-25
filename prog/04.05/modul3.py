from posixpath import split


class Osztaly:
    def __init__(self,nev,fizu,szul_ev,szekhely):
        self.nev = nev
        self.fizu = int(fizu)
        self.szul_ev = int(szul_ev)
        self.szekhely = szekhely 

        print(fizu*fizu)