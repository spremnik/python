import os
import random
 
polja = [1,2,3,4,5,6,7,8,9]
pro =  [[0,1,2], [3,4,5], [6,7,8],  # Vodoravno
        [0,3,6], [1,4,7], [2,5,8],  # Okomito
        [0,4,8], [2,4,6]]           # Koso
korak = 0
igrač = ['X', 'O']
red = random.randint(0,1)

while True:
    znak_igrača = input('Upišite znak s kojim želite igrati (X ili O): ').upper()
    if znak_igrača == 'X' or znak_igrača == 'O':
    	break
    else:
    	print('Unesen je krivi znak.')
    
if igrač[red] == znak_igrača:
	print('Igrač je prvi na potezu.')
else:
	print('Računalo igra prvi potez.')

input('Pritisni tipku ENTER za nastavak.')

def pobriši_zaslon():
    os.system('cls' if os.name == 'nt' else 'clear')

def ispis(p):
    pobriši_zaslon()
    for b in range(9):
        if p[b] == 'X':
            p[b] = '\033[31mX\033[37m'
        elif p[b] == 'O':
            p[b] = '\033[32mO\033[37m'
    print(  ' '*15, 'KRIŽIĆ KRUŽIĆ', '\n'*2, 
            '\t'*2, f' {p[0]} │ {p[1]} │ {p[2]} ', '\n', '\t'*2, '───┼───┼───', '\n',
            '\t'*2, f' {p[3]} │ {p[4]} │ {p[5]} ', '\n', '\t'*2, '───┼───┼───', '\n', 
            '\t'*2, f' {p[6]} │ {p[7]} │ {p[8]} ', '\n'*2,)

def pobjednik(polja, znak, znak_igrača):
    ispis(polja[:])
    if znak == znak_igrača:
        print('\t', ' '*4, '\033[32mIgrač je pobjednik.\033[37m\n')
    else:
        print('\t', ' '*2, '\033[31mRačunalo je pobjednik.\033[37m\n')

def računalo(polja, pro, red, igrač):
	kut = [0, 2, 6, 8]
	if str(polja[4]).isnumeric(): #Srednje polje
		return 5
	else:
		for b in range(8): #Ako postoji dva ista u nizu od računala.
			if [polja[pro[b][0]], polja[pro[b][1]], polja[pro[b][2]]].count(igrač[red]) == 2:
				for br in range(3):
					if isinstance(polja[pro[b][br]], int):
						return pro[b][br] + 1
		for b in range(8): #Ako postoji dva ista u nizu od igrača.
			if [polja[pro[b][0]], polja[pro[b][1]], polja[pro[b][2]]].count(igrač[(red + 1) % 2]) == 2:
				for br in range(3):
					if isinstance(polja[pro[b][br]], int):
						return pro[b][br] + 1
		for b in range(4): #Kutovi.
					if isinstance(polja[kut[b]], int):
						return  kut[b] + 1
		for b in range(9): #Izaberi prvi slobodni u listi polja.
					if isinstance(polja[b], int):
						return  polja[b]
						
while True:
    ispis(polja[:])
    if igrač[red] == znak_igrača:
        unos = input('\t     Unesite broj polja: ')
        if unos.isnumeric():
            unos = int(unos)
        else:
        	unos = 0
    else:
    	unos = računalo(polja, pro, red, igrač)
        
    print('Unos je: ', unos)

    if unos > 0 and unos < 10 and polja[unos-1] != 'X' and polja[unos-1] != 'O':
        polja[unos-1] = igrač[red]
        red = (red + 1) % 2
        korak += 1

    for b in range(8):
        if [polja[pro[b][0]], polja[pro[b][1]], polja[pro[b][2]]].count(polja[pro[b][0]]) == 3:
            pobjednik(polja, polja[pro[b][0]], znak_igrača)
            exit()

    if korak == 9:
        ispis(polja)
        print('\t'*2, '\033[31mNeriješeno!\033[37m\n')
        break
