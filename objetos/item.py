class Item:
   def __init__(self, nombre, tipo, info, precio_base):
      self.nombre = nombre # str
      self.tipo = tipo # str 'a'=alimento o 'b'=bebida
      self.info = info # str if alimento > 'e' 'p' | if bebida> 'p' 'm' 'g'
      self.precio_base = precio_base # float
      self.combos = [] # Array indicando a los combos que pertenece
      self.impuesto = 0.16

   def get_tipo(self):
      if self.tipo == 'a':
         return 'Alimento'
      elif self.tipo == 'b':
         return 'Bebida'
   
   def get_info(self):
      if self.tipo == 'a':
         if self.info == 'e':
            return 'Empaque'
         elif self.info == 'p':
            return 'Preparación'
   
      elif self.tipo == 'b':
         if self.info == 'p':
            return 'Pequeño'
         elif self.info == 'm':
            return 'Mediano'
         elif self.info == 'g':
            return 'Grande'

   def get_precio_base(self):
      return self.precio_base

   def get_precio_total(self):
      return self.precio_base + (self.precio_base*self.impuesto)

   def modificar_algo(self, algo, new):
      if algo == 'n':
         self.nombre = new
      elif algo == 't':
         self.tipo = new
      elif algo == 'i':
         self.info = new
      elif algo == 'p':
         self.precio_base = new