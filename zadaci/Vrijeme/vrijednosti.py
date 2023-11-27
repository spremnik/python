import datetime

class Stvoreni:
    def __init__(self):
        self.temp_doma = [22,-0.01]
        self.vlaz_doma = [46,-0.01]
        self.prosjecna_temperatura = ((-2,3),(1,8),(2,13),
                                      (4,15),(10,20),(13,23),
                                      (15,27),(16,28),(10,22),
                                      (7,15),(2,8),(-1,4))  
        self.prosjecni_tlak =  ((1022,1019),(1032,1025),(1019,1008),
                                (1020,1009),(1023,1013),(1020,1010),
                                (1019,1007),(1018,1006),(1022,1010),
                                (1019,1005),(1023,1017),(1026,1022))  
        self.prosjecna_vlaznost =  ((81,78),(76,69),(68,57),
                                    (65,54),(67,57),(70,60),
                                    (68,55),(72,60),(76,64),
                                    (79,71),(81,75),(82,79))
        
    def temperatura(self):
        mj, se =  self.mjesec_sekunde_danas()
        t = self.prosjecna_temperatura
        if se > 43200:
            return t[mj-1][1] - (t[mj-1][1]-t[mj-1][0]) * ((se - 43200) / 43200)
        else:
            return t[mj-1][0] + (t[mj-1][1]-t[mj-1][0]) * (se / 43200)
        
    def tlak(self):
        mj, se =  self.mjesec_sekunde_danas()
        t = self.prosjecni_tlak
        if se > 43200:
            return t[mj-1][1] + (t[mj-1][0]-t[mj-1][1]) * ((se - 43200) / 43200)
        else:
            return t[mj-1][0] - (t[mj-1][0]-t[mj-1][1]) * (se / 43200)

    def vlaznost(self):
        mj, se =  self.mjesec_sekunde_danas()
        v = self.prosjecna_vlaznost
        if se > 43200:
            return v[mj-1][1] + (v[mj-1][0]-v[mj-1][1]) * ((se - 43200) / 43200)
        else:
            return v[mj-1][0] - (v[mj-1][0]-v[mj-1][1]) * (se / 43200)

    def mjesec_sekunde_danas(self):
        vrijeme = datetime.datetime.now()
        mjesec = vrijeme.month
        sat = vrijeme.hour
        minute = vrijeme.minute
        sekunde = vrijeme.second
        return mjesec, sekunde + minute * 60 + sat * 3600
    
    def temperatura_doma(self):
        if self.temp_doma[0] < 44:
            self.temp_doma[1] = 0.01
        elif self.temp_doma[0] > 66:
            self.temp_doma[1] = -0.01
        self.temp_doma[0] += self.temp_doma[1]
        return self.temp_doma[0]
    
    def vlaznost_doma(self):
        if self.vlaz_doma[0] < 22:
            self.vlaz_doma[1] = 0.01
        elif self.vlaz_doma[0] > 26:
            self.vlaz_doma[1] = -0.01
        self.vlaz_doma[0] += self.vlaz_doma[1]
        return self.vlaz_doma[0]
    
    def tlak_doma(self):
        return self.tlak() + 1
    
    def sat(self):
        vrijeme = datetime.datetime.now()
        sat = vrijeme.hour
        minuta = vrijeme.minute
        sekunda = vrijeme.second
        if minuta < 10:
            minuta = f'0{minuta}'
        if sekunda < 10:
            sekunda = f'0{sekunda}'
        return f'{sat}:{minuta}:{sekunda}'
    
    def nadnevak(self):
        vrijeme = datetime.datetime.now()
        godina = vrijeme.year
        mjesec = vrijeme.month
        dan = vrijeme.day
        return f'{dan}.{mjesec}.{godina}.'
    
    