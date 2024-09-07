class Vehiculo: 
   def __init__ (self, marca : str, combustible : str):
      self.marca = marca
      self.combustible = combustible 
   def encender (self ):
      pass 
   def arrancar (self ):
      pass
carro = Vehiculo ("toyota","corriente")
print (carro)
print (type(carro))
