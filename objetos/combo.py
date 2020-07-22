class Combo:
   def __init__(self, nombre, precio_base, items):
      self.nombre = nombre # str
      self.precio_base = precio_base # float
      self.vendido = 0 # veces vendido
      self.items = items # array indicando cual items hay (solo su nombre property)
      self.impuesto = 0.16

   def get_precio_total(self):
      return self.precio_base + (self.precio_base*self.impuesto)