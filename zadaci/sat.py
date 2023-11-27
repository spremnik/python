import datetime
import time
from dateutil import tz
import os

class Sat:

    def obriši_zaslon(self):
        os.system('cls' if os.name == "nt" else "clear")
        return True

    def vrijeme(self):
        now = datetime.datetime.now()
        zone = ['Europe/Zagreb', 'Asia/Tokyo', 'America/New_York']
        ispis = '\n'
        for zona in zone:
            ispis +=  now.astimezone(tz.gettz(zona)).strftime(f"%H:%M:%S - {zona}\n")
        return ispis
    

def main():
        
    while True:
        sat = Sat()
        sat.obriši_zaslon()
        print(sat.vrijeme())
        time.sleep(1)
       

if __name__ == '__main__':
    main()