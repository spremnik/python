from kocke_tekst import Kocke
import tkinter
import os

class Kocke_sucelje(tkinter.Tk,Kocke):
    def __init__(self,strana=6,kocki=2):
        super().__init__()

        self.podaci(strana, kocki)
        self.prvo_bacanje = True
        self.kraj = False

        self.kocke = {1:None,2:None}
        self.slike = {1:None,2:None} 

        self.title("Kocke igra")
        self.resizable(False, False)

        self.cilj_ispis = self.napravi_oznaku(self,'CILJ: 7 ili 11',32,0,0,2)
        for b in range(2):
            self.slike[b+1] = tkinter.PhotoImage(file=self.putanja('slike\\6.png'))
            self.kocke[b+1] = self.napravi_sliku(self,self.slike[b+1],100,100,1,b)
    
        self.upravljanje = self.napravi_gumb(self,'IGRAJ',20,3,0,2)

        self.mainloop()
            
    def putanja(self, datoteka):
        return r'{}'.format(os.path.dirname(os.path.abspath(__file__))) + f'{chr(92) if os.name == "nt" else "/"}{datoteka.replace("/",chr(92)) if os.name == "nt" else datoteka.replace(chr(92),"/")}'
    
    def napravi_sliku(self, nadrednik, slika, sirina, visina, redak, stupac, raspon=1, razmak=8):
        stavka = tkinter.Canvas(nadrednik, width=sirina,height=visina) 
        stavka.grid(row=redak, column=stupac, padx=razmak, pady=razmak, columnspan=raspon) 
        stavka.create_image( 2, 2, image = slika, anchor = "nw")
        return stavka

    def napravi_oznaku(self, nadrednik, ispis, sirina, redak, stupac, raspon=1, razmak=8):
        stavka = tkinter.Label(nadrednik, text=ispis, width=sirina)
        stavka.grid(row=redak, column=stupac, padx=razmak, pady=razmak, columnspan=raspon)
        return stavka
    
    def napravi_gumb(self, nadrednik, ispis, sirina, redak, stupac, raspon, razmak=8):
        stavka = tkinter.Button(nadrednik, text=ispis, width=sirina)
        stavka.grid(row=redak, column=stupac, padx=razmak, pady=razmak, columnspan=raspon)
        stavka.config(command=lambda:self.igra())
        return stavka
    
    def vrtnja(self):
        v = self.bacanje()
        self.slike[1].config(file=self.putanja(f'slike\\{v[0]}.png'))
        self.slike[2].config(file=self.putanja(f'slike\\{v[1]}.png'))
        return v[0]+v[1]

    def igra(self):
        if self.kraj:
            self.nova_igra()
        elif self.prvo_bacanje:
            self.cilj = self.vrtnja()
            if self.cilj == 7 or self.cilj == 11:
                self.ispis_ishoda('POBJEDA!')
            elif self.cilj == 2 or self.cilj == 3 or self.cilj == 12:
                self.ispis_ishoda('PORAZ!')
            else:
                self.cilj_ispis.config(text=f'NOVI CILJ: {self.cilj}')
            self.prvo_bacanje = False
        else:
            zbroj = self.vrtnja()
            if zbroj == 2 or zbroj == 3 or zbroj == 12:
                self.ispis_ishoda('PORAZ!')
            elif self.cilj == zbroj:
                self.ispis_ishoda('POBJEDA!')

    def ispis_ishoda(self,ishod):
        self.cilj_ispis.config(text=ishod)
        self.upravljanje.config(text='NOVA IGRA')
        self.kraj = True

    def nova_igra(self):
        self.slike[1].config(file=self.putanja(f'slike\\6.png'))
        self.slike[2].config(file=self.putanja(f'slike\\6.png'))
        self.cilj_ispis.config(text='CILJ: 7 ili 11')
        self.upravljanje.config(text='IGRAJ')
        self.prvo_bacanje = True
        self.kraj = False
        

