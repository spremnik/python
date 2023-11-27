from sense_emu import SenseHat
import time


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
Ž = (255,255,150)   

slike = [[
    B,B,B,P,P,B,B,B,
    B,B,P,C,C,P,B,B,
    B,P,C,C,C,C,P,B,
    P,C,Z,C,C,Z,C,P,
    P,C,C,C,C,C,C,P,
    B,P,Z,Z,Z,Z,P,B,
    B,B,P,C,C,P,B,B,
    B,B,B,P,P,B,B,B],[
    B,B,B,P,P,B,B,B,
    B,B,P,C,C,P,B,B,
    B,P,C,C,C,C,P,B,
    P,C,Z,C,C,Z,C,P,
    P,C,C,C,C,C,C,P,
    B,P,Z,C,C,Z,P,B,
    B,B,P,Z,Z,P,B,B,
    B,B,B,P,P,B,B,B],[
    B,B,B,B,P,B,B,B,
    B,B,B,P,P,B,B,B,
    B,B,B,P,P,B,B,B,
    B,B,P,P,P,B,B,B,
    B,B,B,P,B,B,B,B,
    B,B,B,C,B,B,B,B,
    B,B,C,Ž,C,B,B,B,
    B,B,C,Ž,C,B,B,B],[
    B,B,B,B,P,B,B,B,
    B,B,B,P,P,B,B,B,
    B,B,B,P,P,B,B,B,
    B,B,P,P,P,B,B,B,
    B,B,B,P,B,B,B,B,
    B,B,B,C,B,B,B,B,
    B,B,Ž,C,Ž,B,B,B,
    B,B,C,Ž,C,B,B,B],[
    B,B,B,C,B,B,B,B,
    B,B,B,C,B,B,B,B,
    B,B,B,C,B,B,B,B,
    C,C,C,C,C,C,C,C,
    B,B,B,C,B,B,B,B,
    B,B,B,C,B,B,B,B,
    B,B,B,C,B,B,B,B,
    B,B,B,C,B,B,B,B],[
    B,B,B,C,Z,B,B,B,
    B,B,B,C,Z,B,B,B,
    B,B,B,C,Z,B,B,B,
    C,C,C,C,C,C,C,C,
    Z,Z,Z,C,Z,Z,Z,Z,
    B,B,B,C,Z,B,B,B,
    B,B,B,C,Z,B,B,B,
    B,B,B,C,Z,B,B,B],[
    B,B,B,B,B,B,B,B,
    B,B,C,C,B,C,C,B,
    B,C,Ž,Ž,C,Ž,Ž,C,
    B,C,Ž,Ž,Ž,Ž,Ž,C,
    B,B,C,Ž,Ž,Ž,C,B,
    B,B,B,C,Ž,C,B,B,
    B,B,B,B,C,B,B,B,
    B,B,B,B,B,B,B,B],[
    B,B,B,B,B,B,B,B,
    B,B,Ž,Ž,B,Ž,Ž,B,
    B,Ž,C,C,Ž,C,C,Ž,
    B,Ž,C,C,C,C,C,Ž,
    B,B,Ž,C,C,C,Ž,B,
    B,B,B,Ž,C,Ž,B,B,
    B,B,B,B,Ž,B,B,B,
    B,B,B,B,B,B,B,B]]

vrijeme = 0.5
m = 0
while True:
    #Nije gotovo
    dogadaj = sense.stick.get_events()
    sense.set_pixels(slike[m*2])
    time.sleep(vrijeme)
    sense.set_pixels(slike[m*2+1])
    time.sleep(vrijeme)
    if dogadaj.direction == 'left':
        m = 1
    if dogadaj.direction == 'right':
        m = 2
    if dogadaj.direction == 'up':
        m = 3
    if dogadaj.direction == 'down':
        m = 4
   
