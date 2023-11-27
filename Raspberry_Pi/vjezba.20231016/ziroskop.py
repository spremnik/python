from sense_emu import SenseHat
import time

sense = SenseHat()

ziroskop = sense.get_orientation()
print(ziroskop)

roll, pitch, yaw = ziroskop.values()

roll = round(roll,3)
pitch = round(pitch,3)
yaw = round(yaw,3)

print(roll, pitch, yaw)

accelerometer = sense.get_accelerometer_raw().values()
print(accelerometer)

