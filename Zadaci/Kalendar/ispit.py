import datetime
import kalendar

k = kalendar.Kalendar(1,1,1)
datoteka = open('kalendar.txt', 'w')
datoteka.write('')
datoteka.close()
datoteka = open('kalendar.txt', 'a', encoding='utf-8')

tocno = 0
brojcanik = 0
broj_godina = 9999 

print('\nISPITIVANJE TOČNOSTI PODATAKA:\n')
for g in range(broj_godina):
    print(f'\rRačunam:|{"▒" * round(40*((g+1)/broj_godina)):<40}| {(g+1)/broj_godina*100:0.2f} %',end='')
    for m in range(12):
        for d in range(k.dana_u_mjesecu[m+1]):
            k.osvjezi_podatke(d+1,m+1,g+1)
            dan_kalendar = k.dan_u_tjednu(d+1)
            dan_datetime = datetime.date.isoweekday(datetime.date(g+1,m+1,d+1))
            brojcanik += 1
            if dan_kalendar == dan_datetime:
                datoteka.write(f'{f"{d+1}.{m+1}.{g+1}.":>12} {k.nazivi_dana[dan_kalendar-1].capitalize():>12} = {k.nazivi_dana[dan_datetime-1].capitalize()}\n')
                tocno += 1                                    
            else:
                datoteka.write(f'{f"{d+1}.{m+1}.{g+1}.":>12} {k.nazivi_dana[dan_kalendar-1].capitalize():>12} != {k.nazivi_dana[dan_datetime-1].capitalize():<12} >>> GREŠKA <<<\n')
datoteka.write(f'\n GOTOVO! \n\n Točno {tocno} od {brojcanik} dana, {tocno/brojcanik*100:0.2f} %.')
print(f'\n\nGOTOVO! \n\nTočno {tocno} od {brojcanik} dana, {tocno/brojcanik*100:0.2f} %.\n\nOtvori datoteku: kalendat.txt\n')

datoteka.close()