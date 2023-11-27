import sqlite3

class Upis:
    
    def otvori_bazu(self):   
        spoj = sqlite3.connect('vrijeme.db')
        pokazivac = spoj.cursor() 
        return spoj, pokazivac
    
    def napravi_tablicu(self, baza, pokazivac):
        pokazivac.execute('''CREATE TABLE IF NOT EXISTS senzori(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ts TEXT DEFAULT (CURRENT_TIMESTAMP),
                        temperatura_kuca NUMERIC,
                        vlaga_kuca NUMERIC,
                        tlak_kuca NUMERIC,
                        temperatura NUMERIC,
                        vlaga NUMERIC,
                        tlak NUMERIC,
                        icon text);''')
        baza.commit()
	
    def upis_baza(self, baza, pokazivac, podaci):
        pokazivac.execute('''INSERT INTO senzori (
                            temperatura_kuca,
                            vlaga_kuca,
                            tlak_kuca, 
                            temperatura, 
                            vlaga, 
                            tlak, 
                            icon)
                            VALUES (?,?,?,?,?,?,?)''', podaci)
        baza.commit()

    def zatvori_bazu(self, baza):
        baza.close()
