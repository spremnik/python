import os

class Osoba:
    def __init__(self, ime, OIB):
        self.ime = ime
        self.OIB = OIB
    
class Fizicka(Osoba):
    def __init__(self, ime, prezime, OIB ):
        super().__init__(ime, OIB)
        self.prezime = prezime
        self.visina = 0

class Pravna(Osoba): 
    def __init__(self, ime, OIB):
        super().__init__(ime, OIB)
        self.broj_zaposlenih = 0
        self.pocetni_kapital = 0

kupci = []
djelatnici = []

def pobrisi_zaslon():
    '''Obriši ekran'''
    os.system('cls' if os.name == "nt" else "clear")

while True:
    pobrisi_zaslon()
    print('IZBORNIK:\n')
    print('1. Unos Kupaca')
    print('2. Unos djelatnika')
    print('3. Ispis')
    print('4. IZLAZ')
    izbor = input('\nUnesite izbor: ')

    if izbor == '1':
        print('\nVRSTA KUPCA:\n')
        print('1. Fizička osoba')
        print('2. Pravna osoba')
        vrsta_kupca = input('\nUnesite izbor: ')

        if vrsta_kupca == '1':
            print('\nUNOS FIZIČKE OSOBE:\n')
            ime = input('Unesite ime kupca: ')
            prezime = input('Unesite prezime kupca: ')
            OIB = input('Unesite OIB kupca: ')

            kupci.append(Fizicka(ime, prezime, OIB))
            print('Uspješno uneseno.')
            input('Pritisnite ENTER za nastavak.')

        if vrsta_kupca == '2':
            print('\nUNOS PRAVNE OSOBE:\n')
            ime = input('Unesite ime pravne osobe: ')
            OIB = input('Unesite OIB pravne osobe: ')

            kupci.append(Pravna(ime, OIB))
            print('Uspješno uneseno.')
            input('Pritisnite ENTER za nastavak.')

    if izbor == '2':
        print('\nUPIS DJELATNIKA:\n')
        ime = input('Unesite ime djelatnika: ')
        prezime = input('Unesite prezime djelatnika: ')
        OIB = input('Unesite OIB djelatnika: ')

        djelatnici.append(Fizicka(ime, prezime, OIB))
        print('Uspješno uneseno.')
        input('Pritisnite ENTER za nastavak.')

    if izbor == '3':
        print('\nISPIS KUPACA:\n')
        for kupac in kupci:
            if type(kupac) is Fizicka:
                print(kupac.ime, kupac.prezime, kupac.OIB)
            elif type(kupac) is Pravna:
                print(kupac.ime, kupac.OIB)
        
        print('\nISPIS DJELATNIKA:\n')
        for djelatnik in djelatnici:
            print(djelatnik.ime, djelatnik.prezime, djelatnik.OIB)

        input('Pritisnite ENTER za nastavak.')
            
    if izbor == '4':
        break

