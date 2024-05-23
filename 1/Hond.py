class Hond:
  def __init__(self, name, age, soort, geluid):
    self.name = name
    self.age = age
    self.soort = soort
    self.geluid = geluid
  def Hond(self):
    return "{} {} {} {}".format (self.name, self.age, self.soort, self.geluid)
    
def Herder():
  return("Blaf")

def Golden_retriever():
  return("Woef")

def Boxer():
  return("Waff")

h1 = Hond("Botje", 6, "Herder",Herder())
h2 = Hond("Snug", 12, "Golden retriever",Golden_retriever())
h3 = Hond("Pootje",3, "Boxer",Boxer())

print (h1.Hond())
print (h2.Hond())
print (h3.Hond())




























#class Hond:
  #def __init__(self, name, age):
    #self.name = name
    #self.age = age

    #def roep(self):
        #print("roepieroepie")

#h1 = Hond("Snuff", 12)

#print(h1.name)
#print(h1.age)
#h1.roep()





#h2 = Hond("Poot", 5)

#print(h2.name)
#print(h2.age)

#h3 = Hond("Botje", 3)

#print(h3.name)
#print(h3.age)




















#def Waff_functie():
  #  print("woef")
#Waff_functie()











#class Person:
 # def __init__(self, name, age):
   # self.name = name
   # self.age = age
    
 # def roep(self):
  #  print("roepieroepie")

#p1 = Person("John", 36)

#print(p1.name)
#print(p1.age)
#p1.roep()