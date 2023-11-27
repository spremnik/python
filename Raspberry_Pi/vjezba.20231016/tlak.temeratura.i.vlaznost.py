from sense_emu import SenseHat
import time

sense = SenseHat()

temperatura = sense.get_temperature()
print(temperatura)

tlak = sense.get_pressure()
print(tlak)

vlaznost = sense.get_humidity()
print(vlaznost)

