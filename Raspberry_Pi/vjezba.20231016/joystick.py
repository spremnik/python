from sense_emu import SenseHat

sense = SenseHat()

while True:
    #for event in sense.stick.get_events():
    #dogadaj = sense.stick.get_events()
    #if len(dogadaj) != 0:
        #print(dogadaj)
        #print(event.direction, event.action)
    if len(dogadaj) != 0:
        dogadaj = sense.stick.get_events()
        print(dogadaj.direction, dogadaj.action)
