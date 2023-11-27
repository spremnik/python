import tkinter as tk
import sqlite3

class Smartkey(tk.Tk):

    pin = ''
    pin_admin = '1234'
    admin_stranica_nije_prikazana = True
    aktivan = 0
    
    def __init__(self):
        super().__init__()
    
        self.clanovi = [	['Mato', 	'Marić', 	'1111', 1],
							['Luka',	'Babić',	'6833', 0],
							['Ana',		'Jelić',	'7070', 1],
							['Davor',	'Bilić',	'2445', 1],
							['Marija',	'Kovačević','3011', 1],
							['Ivan',	'Horvat',	'1234', 1],
							['Iva',		'Jurić',	'3202', 1],
							['Petra',	'Barišić',	'3266', 1],
							['Josip',	'Radić',	'9226', 1],
							['Dora',	'Perković',	'4408', 1]]
        
        self.napravi_bazu = "CREATE TABLE IF NOT EXISTS clanovi(oznaka_clana INTEGER PRIMARY KEY autoincrement, ime CHAR(64), prezime CHAR(64), pin CHAR(4), aktivan BIT);"
        self.spoj = sqlite3.connect('smartkey.db')
        self.pokazivac = self.spoj.cursor()

        self.pokazivac.execute(self.napravi_bazu)
        self.spoj.commit()
		
        for clan in self.clanovi:
            self.pokazivac.execute(f"SELECT * FROM clanovi WHERE pin = '{clan[2]}';")
            self.podaci = (self.pokazivac.fetchone())
            if self.podaci == None:
                self.pokazivac.execute(f"INSERT INTO clanovi(ime, prezime, pin, aktivan) VALUES('{clan[0]}', '{clan[1]}', '{clan[2]}', '{clan[3]}'); ")
            self.spoj.commit()
      
        self.title("SmartKey")
        self.resizable(False, False)

        self.okvir_vrata = tk.LabelFrame(self)
        self.okvir_vrata.grid(row=0, column=0, padx=5, pady=5)
        self.okvir_vrata.config(borderwidth=2)
               
        self.naziv_okvira_vrata = tk.Label(self.okvir_vrata, text="Panel s gumbima", width=60)
        self.naziv_okvira_vrata.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.gumb_pozvoni = tk.Button(self.okvir_vrata, text=" Pozvoni ", width=10, command=self.pozvoni)
        self.gumb_pozvoni.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        self.ispis_vrata = tk.Label(self.okvir_vrata, text="", height=2)
        self.ispis_vrata.grid(row=1, column=1, rowspan=3, padx=5, pady=5)

        self.gumb_otkljucaj = tk.Button(self.okvir_vrata, text=" Otključaj ", width=10, command=self.otkljucaj)
        self.gumb_otkljucaj.grid(row=3, column=2, padx=5, pady=5, sticky='e')

        self.okvir_pin = tk.LabelFrame(self)
        self.okvir_pin.config(borderwidth=2)
        
        self.naziv_okvira_pin = tk.Label(self.okvir_pin, text="Pin panel", width=60)
        self.naziv_okvira_pin.grid(row=0, column=0, columnspan=18, padx=5, pady=5)

        self.pin_prikaz_1 = tk.Label(self.okvir_pin, borderwidth=1, relief="solid", width = 3)
        self.pin_prikaz_1.grid(row=1, column=0, padx=5, pady=5)

        self.pin_prikaz_2 = tk.Label(self.okvir_pin, borderwidth=1, relief="solid", width = 3)
        self.pin_prikaz_2.grid(row=1, column=1, padx=5, pady=5)

        self.pin_prikaz_3 = tk.Label(self.okvir_pin, borderwidth=1, relief="solid", width = 3)
        self.pin_prikaz_3.grid(row=1, column=2, padx=5, pady=5)

        self.pin_prikaz_4 = tk.Label(self.okvir_pin, borderwidth=1, relief="solid", width = 3)
        self.pin_prikaz_4.grid(row=1, column=3, padx=5, pady=5)
       
        self.gumb_1 = tk.Button(self.okvir_pin, text=" 1 ", command=lambda:self.unos_pina('1'))
        self.gumb_1.grid(row=2, column=0, padx=5, pady=5)

        self.gumb_2 = tk.Button(self.okvir_pin, text=" 2 ", command=lambda:self.unos_pina('2'))
        self.gumb_2.grid(row=2, column=1, padx=5, pady=5)

        self.gumb_3 = tk.Button(self.okvir_pin, text=" 3 ", command=lambda:self.unos_pina('3'))
        self.gumb_3.grid(row=2, column=2, padx=5, pady=5)

        self.gumb_4 = tk.Button(self.okvir_pin, text=" 4 ", command=lambda:self.unos_pina('4'))
        self.gumb_4.grid(row=3, column=0, padx=5, pady=5)

        self.gumb_5 = tk.Button(self.okvir_pin, text=" 5 ", command=lambda:self.unos_pina('5'))
        self.gumb_5.grid(row=3, column=1, padx=5, pady=5)

        self.gumb_6 = tk.Button(self.okvir_pin, text=" 6 ", command=lambda:self.unos_pina('6'))
        self.gumb_6.grid(row=3, column=2, padx=5, pady=5)

        self.gumb_7 = tk.Button(self.okvir_pin, text=" 7 ", command=lambda:self.unos_pina('7'))
        self.gumb_7.grid(row=4, column=0, padx=5, pady=5)

        self.gumb_8 = tk.Button(self.okvir_pin, text=" 8 ", command=lambda:self.unos_pina('8'))
        self.gumb_8.grid(row=4, column=1, padx=5, pady=5)

        self.gumb_9 = tk.Button(self.okvir_pin, text=" 9 ", command=lambda:self.unos_pina('9'))
        self.gumb_9.grid(row=4, column=2, padx=5, pady=5)

        self.gumb_0 = tk.Button(self.okvir_pin, text=" 0 ", command=lambda:self.unos_pina('0'))
        self.gumb_0.grid(row=5, column=1, padx=5, pady=5)
        
        self.gumb_c = tk.Button(self.okvir_pin, text=" C ", command=lambda:self.obrisi_pin())
        self.gumb_c.grid(row=5, column=2, padx=5, pady=5)

        self.poruke_pin = tk.Label(self.okvir_pin, text=" ", width=28, height=12, background='white', borderwidth=1, relief="solid")
        self.poruke_pin.grid(row=1, column=9, columnspan=12, rowspan=5,padx=5, pady=5)

        self.okvir_ulaz_admin = tk.LabelFrame(self)
        self.okvir_ulaz_admin.config(borderwidth=2)
               
        self.naziv_ulaz_admin = tk.Label(self.okvir_ulaz_admin, text="Želite li pokrenuti administraciju sustava?", width=60)
        self.naziv_ulaz_admin.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

        self.gumb_da_admin = tk.Button(self.okvir_ulaz_admin, text=" DA ", width=4, command=self.da)
        self.gumb_da_admin.grid(row=1, column=4, padx=5, pady=5)

        self.gumb_ne_admin = tk.Button(self.okvir_ulaz_admin, text=" NE ", width=4, command=self.ne)
        self.gumb_ne_admin.grid(row=1, column=5, padx=5, pady=5)

        self.okvir_admin = tk.LabelFrame(self)
        self.okvir_admin.config(borderwidth=2)

        self.naziv_okvira_admin = tk.Label(self.okvir_admin, text="Upravljanje dodijeljenim ključevima", width=60)
        self.naziv_okvira_admin.grid(row=0, column=0, columnspan=8, padx=5, pady=5)
        
        self.popis_clanova = tk.Listbox(self.okvir_admin, width=28, height=10, )
        self.popis_clanova.grid(row=1, column=0, columnspan=3, rowspan=5, padx=5, pady=5)
        self.popis_clanova.bind('<<ListboxSelect>>', self.izbor_clana)

        self.napis_ime_clana = tk.Label(self.okvir_admin, text="Ime", anchor='e', justify='right', width=12)
        self.napis_ime_clana.grid(row=1, column=4, columnspan=2, padx=5, pady=5)

        self.napis_prezime_clana = tk.Label(self.okvir_admin, text="Prezime", anchor='e', justify='right', width=12)
        self.napis_prezime_clana.grid(row=2, column=4, columnspan=2, padx=5, pady=5)

        self.napis_pin_clana = tk.Label(self.okvir_admin, text="PIN (4 broja)", anchor='e', justify='right', width=12)
        self.napis_pin_clana.grid(row=3, column=4, columnspan=2, padx=5, pady=5)

        self.napis_prezime_clana = tk.Label(self.okvir_admin, text="Aktivan", anchor='e', justify='right', width=12)
        self.napis_prezime_clana.grid(row=4, column=4, columnspan=2, padx=5, pady=5)

        self.gumb_spremi = tk.Button(self.okvir_admin, text="Spremi", width=8, command=self.spremi)
        self.gumb_spremi.grid(row=5, column=5, padx=5, pady=5)

        self.upis_ime_clan = tk.Entry(self.okvir_admin, width=22)
        self.upis_ime_clan.grid(row=1, column=6, columnspan=2, padx=5, pady=5)

        self.upis_prezime_clan = tk.Entry(self.okvir_admin, width=22)
        self.upis_prezime_clan.grid(row=2, column=6, columnspan=2, padx=5, pady=5)

        self.upis_pin_clan = tk.Entry(self.okvir_admin, width=22)
        self.upis_pin_clan.grid(row=3, column=6, columnspan=2, padx=5, pady=5)

        self.upis_aktivan_clan = tk.Checkbutton(self.okvir_admin, anchor='w', justify='left', command=self.promjeni_aktivnost)
        self.upis_aktivan_clan.grid(row=4, column=6, padx=5, pady=5, sticky='w')

        self.gumb_odustani = tk.Button(self.okvir_admin, text="Odustani", width=8, command=self.ugasi_admin_stranicu)
        self.gumb_odustani.grid(row=5, column=6, padx=5, pady=5)

        self.gumb_izbrisi = tk.Button(self.okvir_admin, text="Izbriši", width=8, command=self.pobrisi)
        self.gumb_izbrisi.grid(row=5, column=7, padx=5, pady=5)
        
        self.poruka_adminu = tk.LabelFrame(self)
        self.poruka_adminu.config(borderwidth=2)

        self.admin_poruka = tk.Label(self.poruka_adminu, text="", width=60, height=5)
        self.admin_poruka.grid(row=0, column=0, columnspan=8, padx=5, pady=5)
    
    def pozvoni(self):
        self.ispis_vrata.config(text='Zvono je aktivirano,\n uskoro će netko doći i otvoriti vrata.')

    def otkljucaj(self):
        self.okvir_pin.grid(row=1, column=0, padx=5, pady=5)
        
    def da(self):
        self.okvir_ulaz_admin.grid_forget()
        self.okvir_admin.grid(row=3, column=0, padx=5, pady=5)
        self.admin_stranica_nije_prikazana = False

        self.popis_clanova.delete(0,10000)
        self.popuni_listu()

    def ne(self):
        self.okvir_ulaz_admin.grid_forget()

    def ispis_pina(self):
        prijenos = ['','','','']
        for b in range(len(self.pin)):
            prijenos[b] = self.pin[b]
        self.pin_prikaz_1.config(text=prijenos[0])
        self.pin_prikaz_2.config(text=prijenos[1])
        self.pin_prikaz_3.config(text=prijenos[2])
        self.pin_prikaz_4.config(text=prijenos[3])

    def unos_pina(self,tipka):
        if len(self.pin) < 4:
            self.pin += tipka
        self.ispis_pina()
        if len(self.pin) >= 4:
            self.provjeri_pin()

    def promjeni_aktivnost(self):
        if self.aktivan == 1:
            self.aktivan=0
        else:
            self.aktivan=1

    def resetiraj_aktivnost(self):
        self.upis_aktivan_clan.deselect()
        self.aktivan = 0

    def obrisi_pin(self):
        self.pin = ''
        self.ispis_pina()
        self.poruke_pin.config(text='')

    def provjeri_pin(self):
        poruka = ''
        if self.pin == self.pin_admin and self.admin_stranica_nije_prikazana:
            poruka += '\nADMIN'
            self.okvir_ulaz_admin.grid(row=4, column=0, padx=5, pady=5)
        self.poruke_pin.config(text=self.upit_pin_baza() + poruka)

    def upit_pin_baza(self):
        self.pokazivac.execute(f"SELECT * FROM clanovi WHERE pin = '{self.pin}';")
        podaci = (self.pokazivac.fetchone())     
        self.spoj.commit()
		    
        if podaci != None and podaci[4] == 1:
            return f'Dobro došli \n{podaci[1]} {podaci[2]}'
        else:
            return 'Nepostojeći korisnik.'

    def ugasi_admin_stranicu(self):
        self.okvir_admin.grid_forget()
        self.admin_stranica_nije_prikazana = True
        self.poruka_adminu.grid_forget()

    def izbor_clana(self, pk):
        izbor = pk.widget.curselection()
        if len(izbor) != 0:
            kazalo = izbor[0]
            clan = pk.widget.get(kazalo)
            pin_izbor = clan.split(' ')[0]
            
            self.pokazivac.execute(f"SELECT * FROM clanovi WHERE pin = '{pin_izbor}';")
            podaci = (self.pokazivac.fetchone())     
            self.spoj.commit()
            
            if podaci != None:
                self.upis_ime_clan.delete(0,100)
                self.upis_ime_clan.insert(0,podaci[1])
                self.upis_prezime_clan.delete(0,100)
                self.upis_prezime_clan.insert(0,podaci[2])
                self.upis_pin_clan.delete(0,100)
                self.upis_pin_clan.insert(0,podaci[3])
                if podaci[4] == 1:
                    self.upis_aktivan_clan.select()
                    self.aktivan = 1
                else:
                    self.upis_aktivan_clan.deselect()
                    self.aktivan = 0
    
    def spremi(self):
        self.poruka_adminu.grid_forget()
        pin_unos = self.upis_pin_clan.get()
        ime_unos = self.upis_ime_clan.get()
        prezime_unos = self.upis_prezime_clan.get()
        aktivan_unos = self.aktivan
       
        if len(pin_unos) == 4 and pin_unos.isdigit():
            self.pokazivac.execute(f"SELECT * FROM clanovi WHERE pin = '{pin_unos}';")
            podaci = (self.pokazivac.fetchone()) 
            self.spoj.commit()
            if podaci == None:
                self.pokazivac.execute(f"INSERT INTO clanovi(ime, prezime, pin, aktivan) VALUES('{ime_unos}', '{prezime_unos}', '{pin_unos}', {aktivan_unos}); ")
            else:
                self.pokazivac.execute(f"UPDATE clanovi SET ime = '{ime_unos}', prezime = '{prezime_unos}', aktivan = {aktivan_unos} WHERE pin = '{pin_unos}' ")
            self.spoj.commit()
        else:
            self.poruka_adminu.grid(row=5, column=0, padx=5, pady=5)
            self.admin_poruka.config(text='Pin mora imati 4 brojke.')
        self.popis_clanova.delete(0,10000)
        self.popuni_listu()

    def popuni_listu(self):
        self.pokazivac.execute("SELECT * FROM clanovi ORDER BY ime DESC;")
        self.podaci = (self.pokazivac.fetchall())     
        self.spoj.commit()

        if self.podaci != None:
            for clan in self.podaci:
                self.popis_clanova.insert(0, f'{clan[3]} {clan[1]} {clan[2]}')

    def pobrisi(self):
        self.poruka_adminu.grid_forget()
        pin_unos = self.upis_pin_clan.get()

        self.pokazivac.execute(f"DELETE FROM clanovi WHERE pin = '{pin_unos}'; ")
        self.spoj.commit()

        self.popis_clanova.delete(0,10000)
        self.popuni_listu()
        self.resetiraj_aktivnost()
    
