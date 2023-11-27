import urllib.request
import urllib.parse

stranice = ['https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html',
            'https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html']

knjige = {}

najjeftinija = ''
najskuplja = '' 


def prikupi_podatke(stranica):
    veza = urllib.request.urlopen(stranica)
    sadržaj = veza.read().decode()
    podaci = {}
    while True:
        naslov = sadržaj.find('title="')
        if naslov != -1:
            sadržaj = sadržaj[naslov + len('title="'):]
            kazalo = sadržaj.find('">')
            knjiga = sadržaj[:kazalo]
            početak_cijene = sadržaj.find('price_color">£')
            sadržaj = sadržaj[početak_cijene + len('price_color">£'):]
            kazalo = sadržaj.find('</p>')
            cijena = float(sadržaj[:kazalo])
            podaci.update({knjiga:cijena}) 
        else:
            return podaci

for stranica in stranice:
    knjige.update(prikupi_podatke(stranica))

for knjiga in knjige:
    if najjeftinija != '' and  najskuplja != '':
        if knjige[knjiga] < knjige[najjeftinija]:
            najjeftinija = knjiga
        if knjige[knjiga] > knjige[najskuplja]:
            najskuplja = knjiga
    else:
        najjeftinija = najskuplja = knjiga

        
izvještaj = f'Knjiga {najjeftinija} je najjeftinija u skupini "Mystery" po cijeni od {knjige[najjeftinija]} £, a knjiga {najskuplja} je najskuplja po cijeni od {knjige[najskuplja]} £.'
  
print(izvještaj)

datoteka = open('knjige.txt', 'w')
datoteka.write(izvještaj)
datoteka.close()

obrnute_knjige = {}
for knjiga in knjige:
    obrnute_knjige.update({knjige[knjiga]:knjiga})

razvrstane_cijene = sorted(obrnute_knjige)
podaci = ''
for cijene in razvrstane_cijene:
    podaci += f'£{cijene:.2f}\t {obrnute_knjige[cijene]}\n'

datoteka = open('knjige.razvrstane.po.cijeni.txt', 'w')
datoteka.write(podaci)
datoteka.close()
