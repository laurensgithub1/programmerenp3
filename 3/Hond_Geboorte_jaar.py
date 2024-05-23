import datetime

class Hond:

    def __init__(self, naam, geboortejaar):
        self.naam = naam
        self.geboortejaar = geboortejaar
        self.leeftijd = self.berekenleeftijd()

    def berekenleeftijd(self):
        huidigjaar = datetime.datetime.now().year
        leeftijd = huidigjaar - self.geboortejaar
        return leeftijd

    def __str__(self):
        return f"{self.naam} is {self.leeftijd} jaar oud en komt uit het geboortejaar {self.geboortejaar}."
    
hond1 = Hond("Bello", 2018)

print(hond1)
print("jo")