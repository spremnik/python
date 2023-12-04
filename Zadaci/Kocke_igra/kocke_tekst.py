import random
import os

class Kocke:
    def __init__(self,broj_stranica=6, broj_kocki=2):
        self.podaci(broj_stranica,broj_kocki)
        self.nova_igra()

        while 1:
            self.igra()

    def bacanje(self):
        return [self.slucajni() for b in range(self.broj_kocki)]

    def slucajni(self):
        return random.randrange(1,self.broj_stranica+1) 
    
    def podaci(self,broj_stranica=6,broj_kocki=2):
        self.broj_stranica = broj_stranica
        self.broj_kocki = broj_kocki
        
    def vrtnja(self):
        v = self.bacanje()
        self.bacene_kocke = f'[{v[0]}] [{v[1]}]'
        return v[0]+v[1]

    def igra(self):
        if self.kraj:
            self.nova_igra()
        elif self.prvo_bacanje:
            self.cilj = self.vrtnja()
            if self.cilj == 7 or self.cilj == 11:
                self.ishod_tekst('POBJEDA!')
            elif self.cilj == 2 or self.cilj == 3 or self.cilj == 12:
                self.ishod_tekst('PORAZ!')
            else:
                self.ispis_cilj = f'NOVI CILJ: {self.cilj}'
                self.ispis()
            self.prvo_bacanje = False
        else:
            zbroj = self.vrtnja()
            if zbroj == 2 or zbroj == 3 or zbroj == 12:
                self.ishod_tekst('PORAZ!')
            elif self.cilj == zbroj:
                self.ishod_tekst('POBJEDA!')
            else:
                self.ispis()

    def pritisni_tipku(self,ispis='Pritisni ENTER za nastavak;'):
        input(ispis)

    def ishod_tekst(self,ishod):
        self.ispis_cilj = ishod
        self.ispis('',False)
        self.kraj = True

    def nova_igra(self):
        self.ispis_cilj = 'Cilj: 7 ili 11'
        self.bacene_kocke = '# #'
        self.prvo_bacanje = True
        self.kraj = False
        self.ispis('Pritisni ENTER za početak;')

    def ispis(self,poruka='Pritisni ENTER za nastavak;',tipka=True):
        self.pobriši_zaslon()
        print('< KOCKE IGRA >\n')
        print(self.ispis_cilj,self.bacene_kocke,'',sep='\n\n')
        if tipka:
            self.pritisni_tipku(poruka)
        else:
            unos = input('Nova igra (da/ne): ')
            if unos == 'ne':
                exit(0)

    def pobriši_zaslon(self):
        os.system('cls' if os.name == 'nt' else 'clear')