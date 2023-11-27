from sense_emu import SenseHat

sense = SenseHat()
#sense.show_message('Nikola')
plavo = (0,0,255)
pozadina = (0, 255, 0)
"""
while 1:
    sense.show_message('Python', 10, plavo, pozadina)

sense.clear()
"""

#sense.set_pixel(0,2, (0,255,0))

C = (255,0,0) 
Z = (0,255,0) 
P = (0,0,255) 
B = (255,255,255) 

slika = [
    Z,Z,Z,Z,Z,Z,Z,Z,
    C,C,C,C,C,C,C,C,
    C,C,C,C,C,C,C,C,
    B,B,B,B,B,B,B,B,
    B,B,B,B,B,B,B,B,
    P,P,P,P,P,P,P,P,
    P,P,P,P,P,P,P,P,
    Z,Z,Z,Z,Z,Z,Z,Z]

sense.set_pixels(slika)

kutevi = [0, 90, 0, 270]
for kut in kutevi:
    sense.rotation(kut)
