class Tour:
   def __init__(self, nombre, precio, max_personas, tiempo, cupos, descuentos='Ninguno', info=None):
      self.nombre = nombre # Str
      self.precio = precio # Float
      self.max_personas = max_personas # Int o None si infinito
      self.tiempo = tiempo # Str
      self.cupos = cupos # int o None si infinito
      self.info = info # Str
      self.descuentos = descuentos # Str
      self.cupos_ocupados = 0 # Int
      self.disponibilidad = True
   
   def get_disponibilidad(self):
      if self.cupos_ocupados >= self.cupos:
         self.disponibilidad = True
         return False
      else:
         self.disponibilidad = False
         return True
   
   def get_max_persona(self):
      if self.max_personas > 999:
         return 'Ilimitado'
      else:
         return self.max_personas
   
   def get_costo(self, party):
      boleto_cost = self.precio
      costo = 0

      if self.descuentos: # Checkear si descuentos existen
         for boleto in range(party):
            if boleto + 1 > 2: # Boletos de 3 o mas personas
               costo += boleto_cost - (boleto_cost*.1) # -%10
            else:
               costo += boleto_cost

      return costo

   def ocupar_cupos(self, n):
      self.cupos_ocupados += n
   
   def get_cupos_disponibles(self):
      if self.cupos > 1000:
         return 'Ilimitado'
      return self.cupos - self.cupos_ocupados
   
   def update_tour(self):
      with open('data_tours.txt', 'r') as data:
         for line in data:
            if line.split('|')[0] == self.nombre:
               try:
                  self.cupos_ocupados = int(line.split('|')[1])
               except:
                  print('El arcivo "data_tours.txt" esta corrupto. Intente borrarolo o generar uno nuevo. Los datos se borraran tambien... :(')