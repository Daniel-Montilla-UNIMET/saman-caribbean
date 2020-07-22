class Habitacion:
   def __init__(self, identificador, capacidad, tipo, costo, crucero_padre, ocupado=False, info=''):
      self.identificador = identificador
      self.capacidad = capacidad
      self.tipo = tipo
      self.costo = costo
      self.ocupado = ocupado
      self.crucero_padre = crucero_padre
      self.info = info
      self.personas = []
   
   def set_ocupado(self, state):
      self.ocupado = state

   def get_info(self):
      if self.tipo == 'Sencillo':
         return 'Si puede tener servicio a la habitación'
      elif self.tipo == 'Premium':
         return 'Si posee vista al mar'
      elif self.tipo == 'VIP':
         return 'Sí puede albergar fiestas privadas'

   def agregar_personas(self, persona):
      self.personas.append(persona)
   
   def get_id(self):
      if self.tipo == 'simple':
         return f'S{self.identificador}'
      elif self.tipo == 'premium':
         return f'P{self.identificador}'
      elif self.tipo == 'vip':
         return f'V{self.identificador}'

   def add_parent_crucero(self, nombre):
      self.crucero_padre = nombre