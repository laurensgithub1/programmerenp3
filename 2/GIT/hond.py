import datetime

class Hond:
    # Constructor
    def __init__(self, naam, geboortejaar):
        self.naam = naam
        self.geboortejaar = geboortejaar
        self.leeftijd = datetime.datetime.now().year - geboortejaar

    def __str__(self):
        return f"{self.naam} is {self.leeftijd} jaar oud en zijn geboortejaar is in{self.geboortejaar}."

hond1 = Hond("Bello", 2016)
print(hond1)
print("jo")