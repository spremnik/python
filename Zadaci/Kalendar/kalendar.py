class Kalendar:

    def __init__(self, dan_u_mjesecu, mjesec, godina):
        self.nazivi_mjeseca = ('siječanj', 'veljača', 'ožujak', 'travanj', 'svibanj', 'lipanj', 'srpanj', 'kolovoz', 'rujan', 'listopad', 'studeni', 'prosinac')
        self.nazivi_dana = ('ponedjeljak', 'utorak', 'srijeda', 'četvrtak', 'petak', 'subota', 'nedjelja')
        self.dana_u_mjesecu = [0,31,28,31,30,31,30,31,31,30,31,30,31] 
        
        self.osvjezi_podatke(dan_u_mjesecu, mjesec, godina)
    
    def ispis(self,crta = '═'):    
        ispis = f'{self.nazivi_mjeseca[self.mjesec-1].capitalize()} {self.godina}\n'
        ispis += crta * 27 + '\n'
        for dan in range(7):
            ispis += f'{self.nazivi_dana[dan][:3].capitalize()} '
        ispis += '\n' + crta * 27
        dan_u_tjednu = self.dan_u_tjednu()
        for d in range(42):
            dan_ispis = ''
            if d % 7 == 0:
                ispis += '\n' 
            if dan_u_tjednu <= d + 1:
                dan_ispis = d - dan_u_tjednu + 2
            if d - dan_u_tjednu >= self.dana_u_mjesecu[self.mjesec]-1:
                break
            if d - dan_u_tjednu + 2 == self.dan:
                ispis += f'[{dan_ispis: >2}]'
            else:
                ispis += f'{dan_ispis: >3} '
        if d % 7 != 0:
            ispis += '\n' 
        ispis += crta * 27 + '\n'
        return ispis

    def dan_u_tjednu(self,dan_u_mjesecu=1):
        dan = (self.dani_po_godinama() + self.dani_po_mjesecima() + dan_u_mjesecu) % 7 
        if dan == 0:
            return 7
        return dan
    
    def dani_po_mjesecima(self,dani=0):
        for mjesec in range(self.mjesec):
            dani += self.dana_u_mjesecu[mjesec] 
        return dani
        
    def dani_po_godinama(self):
        return (self.godina - 1) * 365 + (self.godina - 1) // 4 - (self.godina - 1) // 100 + (self.godina - 1) // 400 

    def osvjezi_podatke(self,dan_u_mjesecu,mjesec,godina):
        self.dan = dan_u_mjesecu
        self.mjesec = mjesec
        self.godina = godina
        if godina % 4 == 0 and godina % 100 != 0 or godina % 400 == 0: 
            self.dana_u_mjesecu[2] = 29
        else:
            self.dana_u_mjesecu[2] = 28
