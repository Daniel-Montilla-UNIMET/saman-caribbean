# Importando Archivo requeridos
from utilidades.operaciones import es_primo
from utilidades.operaciones import es_abundante

class Persona:
   def __init__(self, nombre, cedula, edad, discapacidad, habitacion, boleto_costo):
      self.nombre = nombre # Str
      self.cedula = cedula # Int
      self.edad = edad # Int
      self.discapacidad = discapacidad # Bool
      self.habitacion = habitacion # str (ID)
      self.boleto_costo = boleto_costo # Float

   def get_costo_boleto(self):
      descuento = 0.0 # Manega valor numerico
      descuentos = [] # Manega cuales descuentos se aplican

      # Agregando descuentos
      if es_primo(self.cedula):
         descuento += 0.1
         descuentos.append('Cedula es un numero primo (-10%)')
      
      if es_abundante(self.cedula):
         descuento += 0.15
         descuentos.append('Cedula es un numero abundante (-15%)')

      if self.discapacidad:
         descuento += 0.3
         descuentos.append('Persona tiene discapacidad (-30%)')

      # Aplicando descuentos
      costo = self.boleto_costo - (self.boleto_costo * descuento)

      return [costo, descuentos]

   def get_upgrade(self): # Determinar si es de la 3ra edad
      if self.edad > 65:
         return True
      else:
         return False
      