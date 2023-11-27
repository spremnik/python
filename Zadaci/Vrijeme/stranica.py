import requests

class Stvarni:
    def __init__(self):
        self.veza = "https://weatherapi-com.p.rapidapi.com/current.json"
        
        self.upit = {"q":"Zagreb HR"}
        
        self.zaglavlja = {
	        "X-RapidAPI-Key": "9ff975df03msh5236528bbfa175dp1471ecjsn80d1e1032ef5",
	        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

    def odgovor(self):
        response = requests.get(self.veza, headers=self.zaglavlja, params=self.upit)
        temperatura = response.json()['current']['temp_c']
        vlaga = response.json()['current']['humidity']
        tlak = response.json()['current']['pressure_mb']
        return temperatura, vlaga, tlak

