import tkinter

class Enigma(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.ispis = {}
        self.uticnice = {}
        self.broj_koluta = []
        self.kolut_slovo = []
        self.kolut = [] 

        self.abeceda =       'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.tipkovnica =    'QWERTZUIOASDFGHJKPYXCVBNML'
        self.reflektor =     'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        self.kolutovi = (   ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'UWYGADFPVZBECKMTHXSLRINQOJ'),
                            ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'AJPCZWRLFBDKOTYUQGENHXMIVS'),
                            ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'TAGBPCSDQEUFVNZHYIXJWLRKOM'),
                            ('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'HZWVARTNLGUPXQCEJMBSKDYOIF'),
                            ('VZBRGITYUPSDNHLXAWMJQOFECK', 'QCYLXWENFTZOSMVJUDKGIARPHB')) 
        self.slovo_prijenosa = ('Q','E','V','J','Z')

        self.stanje_kolutova = [0,0,0]
        self.vrsta_kolutova = [0,1,2]
        self.prespoj_uticnica = {}
        self.polucak = ''
        self.izabrana_uticnica = False

        self.rimski = ('I','II','III','IV','V')
        
        self.title("Enigma")
        self.resizable(False, False)
        
        self.okvir_kolutovi = self.napravi_okvir(self,'Postavke',1,0)
        self.okvir_ispis = self.napravi_okvir(self,'Ispis',2,0)
        self.okvir_unos = self.napravi_okvir(self,'Tipkovnica',3,0)
        self.okvir_uticnice = self.napravi_okvir(self,'Utičnice',4,0)
        
        for b in range(3):
            self.napravi_gumb('v',self.okvir_kolutovi,'ᐊ',3,1,b*3,b)
            self.broj_koluta.append(self.napravi_oznaku(self.okvir_kolutovi,self.rimski[self.vrsta_kolutova[b]],3,1,b*3+1))
            self.napravi_gumb('v',self.okvir_kolutovi,'ᐅ',3,1,b*3+2,b,1)
            
            self.napravi_gumb('k', self.okvir_kolutovi,'▲',3,2,b*3+1,b,1)
            self.kolut.append(self.napravi_oznaku(self.okvir_kolutovi,self.stanje_kolutova[b]+1,3,3,b*3+1))
            self.napravi_gumb('k', self.okvir_kolutovi,'▼',3,4,b*3+1,b)

        self.upisano = self.napravi_unos(self.okvir_ispis,self.polucak,67,4,0,18)

        for b in range(len(self.tipkovnica)):
            self.ispis.update({self.tipkovnica[b]:self.napravi_oznaku(self.okvir_ispis,self.tipkovnica[b],3,b//9,(b*2)%18)})
            self.napravi_gumb('t', self.okvir_unos,self.tipkovnica[b],3,b//9,(b*2)%18)
            self.uticnice.update({self.tipkovnica[b]:self.napravi_gumb('u', self.okvir_uticnice,self.tipkovnica[b],3,b//9,(b*2)%18)})
            self.prespoj_uticnica.update({self.tipkovnica[b]:self.tipkovnica[b]})
        
        self.mainloop()

    def napravi_okvir(self, nadrednik, ime_okvira, redak, stupac, razmak=8):
        stavka = tkinter.LabelFrame(nadrednik,text=ime_okvira)
        stavka.grid(row=redak, column=stupac, padx=razmak, pady=razmak)
        stavka.config(borderwidth=2)
        return stavka

    def napravi_gumb(self, vrsta, nadrednik, ispis, sirina, redak, stupac, kolut = 0, smjer = -1, razmak=8):
        stavka = tkinter.Button(nadrednik, text=ispis, width=sirina)
        stavka.grid(row=redak, column=stupac, padx=razmak, pady=razmak)
        if vrsta == 't': 
            stavka.config(command=lambda:self.unos(ispis))
        elif vrsta == 'u':
            stavka.config(command=lambda:self.prikljuci(ispis))
        elif vrsta == 'k':
            stavka.config(command=lambda:self.postavi_stanje_kolutova(kolut, smjer))
        elif vrsta == 'v':
            stavka.config(command=lambda:self.postavi_vrstu_kolutova(kolut, smjer))
        return stavka

    def napravi_oznaku(self, nadrednik, ispis, sirina, redak, stupac, raspon=1, razmak=8):
        stavka = tkinter.Label(nadrednik, text=ispis, width=sirina)
        stavka.grid(row=redak, column=stupac, padx=razmak, pady=razmak, columnspan=raspon)
        stavka.config(background='white', borderwidth=1, relief='solid')
        return stavka
    
    def napravi_unos(self, nadrednik, ispis, sirina, redak, stupac, raspon=1, razmak=8):
        stavka = tkinter.Entry(nadrednik, text=ispis, width=sirina)
        stavka.grid(row=redak, column=stupac, padx=razmak, pady=razmak, columnspan=raspon)
        stavka.config(state='normal')
        return stavka

    def obrisi_ispis(self):
        for slovo in self.ispis:
            self.ispis[slovo].config(background='white')
    
    def pokretanje_kolutova(self):
        if self.abeceda.find(self.slovo_prijenosa[self.vrsta_kolutova[2]]) == self.stanje_kolutova[2]:
            if self.abeceda.find(self.slovo_prijenosa[self.vrsta_kolutova[1]]) == self.stanje_kolutova[1]:
                self.stanje_kolutova[0] = (self.stanje_kolutova[0] + 1) % 26
                self.kolut[0].config(text=self.stanje_kolutova[0] + 1)
            self.stanje_kolutova[1] = (self.stanje_kolutova[1] + 1) % 26
            self.kolut[1].config(text=self.stanje_kolutova[1] + 1)
        self.stanje_kolutova[2] = (self.stanje_kolutova[2] + 1) % 26
        self.kolut[2].config(text=self.stanje_kolutova[2] + 1)
        
    def unos(self,tipka):
        self.obrisi_ispis()
        self.pokretanje_kolutova()
        zagonetka = self.zagonetka(tipka)
        self.polucak += zagonetka
        self.upisano.delete(0,tkinter.END)
        self.upisano.insert(0,self.polucak)
        self.ispis[zagonetka].config(background='yellow')

    def prikljuci(self,tipka):
        if self.izabrana_uticnica: 
            if self.prespoj_uticnica[tipka] != tipka:
                self.uticnice[self.prespoj_uticnica[tipka]].config(background='#f0f0f0', fg='black', text=self.prespoj_uticnica[tipka])
                self.prespoj_uticnica[self.prespoj_uticnica[tipka]] = self.prespoj_uticnica[tipka]
            if self.izabrana_uticnica == tipka:
                self.uticnice[tipka].config(background='#f0f0f0', fg='black', text=tipka)
                self.prespoj_uticnica[self.izabrana_uticnica]=tipka
            else:
                self.uticnice[tipka].config(background='lightgrey', fg='black', text=f'{tipka}-{self.izabrana_uticnica}')
                self.uticnice[self.izabrana_uticnica].config(background='lightgrey', fg='black', text=f'{self.izabrana_uticnica}-{tipka}')
                self.prespoj_uticnica[tipka]=self.izabrana_uticnica
                self.prespoj_uticnica[self.izabrana_uticnica]=tipka
            self.izabrana_uticnica = False
        else:
            if self.prespoj_uticnica[tipka] != tipka:
                self.uticnice[self.prespoj_uticnica[tipka]].config(background='#f0f0f0', fg='black', text=self.prespoj_uticnica[tipka])
                self.prespoj_uticnica[self.prespoj_uticnica[tipka]] = self.prespoj_uticnica[tipka]
            self.uticnice[tipka].config(background='grey', fg='white', text=tipka)
            self.izabrana_uticnica = tipka

    def postavi_stanje_kolutova(self, broj_koluta, smjer = -1):
        self.stanje_kolutova[broj_koluta] = (self.stanje_kolutova[broj_koluta] + smjer) % 26
        self.kolut[broj_koluta].config(text=self.stanje_kolutova[broj_koluta] + 1)

    def postavi_vrstu_kolutova(self, broj_koluta, smjer = -1):
        for b in range(5): 
            vrsta = (self.vrsta_kolutova[broj_koluta] + b * smjer) % 5
            if vrsta not in self.vrsta_kolutova:
                self.vrsta_kolutova[broj_koluta] = vrsta
                break
        self.broj_koluta[broj_koluta].config(text=self.rimski[self.vrsta_kolutova[broj_koluta]])

    def zagonetka(self,tipka):
        zagonetka = self.prespoj_uticnica[tipka]
        broj_ulaz = self.abeceda.find(zagonetka)
        for b in range(2,-1,-1):
            zagonetka = self.kolutovi[self.vrsta_kolutova[b]][0][broj_ulaz-self.stanje_kolutova[b]%26]
            broj_ulaz = (self.abeceda.find(zagonetka)+self.stanje_kolutova[b])%26
        zagonetka = self.reflektor[broj_ulaz]
        broj_ulaz = self.abeceda.find(zagonetka)
        for b in range(3):
            zagonetka = self.kolutovi[self.vrsta_kolutova[b]][1][broj_ulaz-self.stanje_kolutova[b]%26]
            broj_ulaz = (self.abeceda.find(zagonetka)+self.stanje_kolutova[b])%26
        zagonetka = self.abeceda[broj_ulaz]
        zagonetka = self.prespoj_uticnica[zagonetka]
        
        return zagonetka