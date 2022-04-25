class Kategoria:
    def __init__(self,nev,varos,orszag,magassag,emelet,epult):
        self.nev = nev
        self.varos = varos
        self.orszag = orszag
        self.magassag = float(magassag.replace(',', '.'))
        self.emelet = int(emelet)
        self.epult = int(epult)