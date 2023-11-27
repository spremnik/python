import os
 
polja = [1,2,3,4,5,6,7,8,9]
pro =  [[0,1,2], [3,4,5], [6,7,8],  # Vodoravno
        [0,3,6], [1,4,7], [2,5,8],  # Okomito
        [0,4,8], [2,4,6]]           # Koso
korak = 0
igrač = ['X', 'O']
red = 0

def pobriši_zaslon():
    os.system('cls' if os.name == 'nt' else 'clear')

def ispis(p):
    pobriši_zaslon()
    for b in range(9):
        if p[b] == 'X':
            p[b] = '\033[32mX\033[37m'
        elif p[b] == 'O':
            p[b] = '\033[31mO\033[37m'
    print(  ' '*15, 'KRIŽIĆ KRUŽIĆ', '\n'*2, 
            '\t'*2, f' {p[0]} │ {p[1]} │ {p[2]} ', '\n', '\t'*2, '───┼───┼───', '\n',
            '\t'*2, f' {p[3]} │ {p[4]} │ {p[5]} ', '\n', '\t'*2, '───┼───┼───', '\n', 
            '\t'*2, f' {p[6]} │ {p[7]} │ {p[8]} ', '\n'*2,
            '\t', 'Igrač 1 (X) - Igrač 2 (O)', '\n')

def pobjednik(polja, znak):
    ispis(polja[:])
    if znak == 'X':
        print( '\n\t\033[32mPobjednik je igrač 1 (X).\033[37m\n')
    else:
        print( '\n\t\033[32mPobjednik je igrač 2 (O).\033[37m\n')

while True:
    ispis(polja[:])
    unos = input(f'\tUnesite broj polja (Igrač {red + 1}):')

    if unos.isnumeric():
        unos = int(unos)
    else:
        unos = 0

    if unos >= 1 and unos <=9 and polja[unos-1] != 'X' and polja[unos-1] != 'O':
        polja[unos-1] = igrač[red]
        red = (red + 1) % 2
        korak += 1

    for b in range(8):
        if [polja[pro[b][0]], polja[pro[b][1]], polja[pro[b][2]]].count(polja[pro[b][0]]) == 3:
            pobjednik(polja, polja[pro[b][0]])
            exit()

    if korak == 9:
        ispis(polja)
        print('\n\t\t\033[31mNeriješeno!\033[37m\n')
        break
