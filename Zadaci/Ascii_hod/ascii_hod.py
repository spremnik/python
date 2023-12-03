import os
import time

class Ascii_hod:
    def __init__(self,naziv_datoteke='slike.pod'):

        self.podaci = self.izbrisi_okvir(self.citaj_datoteku(naziv_datoteke))
        self.pokreni(self.podaci)
    
    def pokreni(self,podaci,duljina=1161,slika=0):
        while 1:
            print(podaci[slika*duljina:(slika+1)*duljina])
            print('\033[F'*29, '\r', sep='')
            slika = (slika + 1) % 12
            time.sleep(1/10)

    def citaj_datoteku(self,naziv_dadoteke):
        datoteka = open(self.putanja(naziv_dadoteke), 'r', encoding='utf-8')
        sadrzaj = datoteka.read()
        datoteka.close()
        return sadrzaj
    
    def putanja(self, datoteka):
        return r'{}'.format(os.path.dirname(os.path.abspath(__file__))) + f'\{datoteka}'
    
    def izbrisi_okvir(self,podaci):
        znakovi = ['┌','─','┐','│','└','┘']
        for znak in znakovi:
            podaci = podaci.replace(znak, ' ')
        return podaci