import tkinter
import os

import vrijednosti
import podaci
#import stranica

class Vrijeme(tkinter.Tk, vrijednosti.Stvoreni, podaci.Upis): #stranica.Stvarni

    def __init__(self):
        super(Vrijeme, self).__init__()
        vrijednosti.Stvoreni.__init__(self)
        self.title("Vrijeme")
        self.geometry("320x320")
        self.resizable(False, False)

        self.spoj, self.pokazivac = self.otvori_bazu()
        self.napravi_tablicu(self.spoj, self.pokazivac)
        
        self.prikaz_nadnevak = self.napravi_oznaku(self,self.nadnevak(),12,0,0,12,1)
        self.prikaz_sat = self.napravi_oznaku(self,self.sat(),8,0,2,12,1)
        self.napravi_oznaku(self,'Doma',8,1,0,12,3)
        self.unutarnja_temperatura = self.napravi_oznaku(self,f'{self.temperatura_doma():0.2f} °c',8,2,0,12,1)
        self.unutarnji_tlak = self.napravi_oznaku(self,f'{self. tlak_doma():0.2f} hPa',10,2,1,12,1)
        self.unutarnja_vlaznost = self.napravi_oznaku(self,f'{self.vlaznost_doma():0.2f} %',8,2,2,12,1)
        self.napravi_oznaku(self,'Dvorište',8,3,0,12,3)
        self.vanjska_temperatura = self.napravi_oznaku(self,f'{self.temperatura():0.2f} °c',8,4,0,12,1)
        self.vanjska_tlak = self.napravi_oznaku(self,f'{self. tlak():0.2f} hPa',10,4,1,12,1)
        self.vanjska_vlaznost = self.napravi_oznaku(self,f'{self.vlaznost():0.2f} %',8,4,2,12,1)

        self.slika = tkinter.PhotoImage(file=self.izaberi_sliku())
        self.platno = tkinter.Canvas(self, width=112,height=96) 
        self.platno.grid(row=5, column=0, padx=8, pady=8, columnspan=3)  
        self.platno.create_image( 0, 0, image = self.slika, anchor = "nw")

        self.after(1000,self.ponovi)

    def putanja_slike(self, slika):
        return r'{}'.format(os.path.dirname(os.path.abspath(__file__))) + '\slike' + f'\{slika}'

    def napravi_oznaku(self, nadredeni, ispis, sirina, redak, stupac, velicina_teksta=12, raspon=1, razmak=8):
        stavka = tkinter.Label(nadredeni, text=ispis, width=sirina, font=('Halvetica',velicina_teksta))
        stavka.grid(row=redak, column=stupac, padx=razmak, pady=razmak, columnspan=raspon)
        stavka.config(background='#f0f0f0', borderwidth=0, relief='solid')
        return stavka

    def ponovi(self):
        temperatura_doma = self.temperatura_doma()
        vlaga_doma = self.vlaznost_doma()
        tlak_doma = self.tlak_doma()
        temperatura = self.temperatura()
        tlak = self.tlak()
        vlaznost = self.vlaznost()
        self.prikaz_sat.config(text=self.sat())
        self.prikaz_nadnevak.config(text=self.nadnevak())
        self.unutarnja_temperatura.config(text=f'{temperatura_doma:0.2f} °c')
        self.unutarnji_tlak.config(text=f'{tlak_doma:0.2f} hPa')
        self.unutarnja_vlaznost.config(text=f'{vlaga_doma:0.2f} %')
        self.vanjska_temperatura.config(text=f'{temperatura:0.2f} °c')
        self.vanjska_tlak.config(text=f'{tlak:0.2f} hPa')
        self.vanjska_vlaznost.config(text=f'{vlaznost:0.2f} %')
        
        self.slika = tkinter.PhotoImage(file=self.izaberi_sliku())   
        self.platno.create_image( 0, 0, image = self.slika, anchor = "nw")

        self.upis_baza(self.spoj, self.pokazivac, (temperatura_doma, vlaga_doma, tlak_doma, temperatura, tlak, vlaznost, self.izaberi_sliku()))

        self.after(1000,self.ponovi)
  
    def izaberi_sliku(self):
        vanjska_temp = self.temperatura()
        if vanjska_temp > 22:
            return self.putanja_slike('majica.png')
        elif vanjska_temp <= 22 and vanjska_temp >= 12:
            return self.putanja_slike('jakna.png')
        elif vanjska_temp <= 12 and vanjska_temp >= 0:
            return self.putanja_slike('zimska.png')
        else:
            return self.putanja_slike('kapa.png')

vrijeme = Vrijeme()
vrijeme.mainloop()
