class Crucero:
   def __init__(self, nombre, ruta, fecha_salida, costo_boletos, alojamiento, capcaidad_habitaciones):
      self.nombre = nombre # Str
      self.ruta = ruta # Arr
      self.fecha_salida = fecha_salida # Str
      self.costo_boletos = costo_boletos # Dict
      self.alojamiento = alojamiento # Dict
      self.capcaidad_habitaciones = capcaidad_habitaciones # Dict
      self.pisos = [] # Lista con objectos pisos
   
   def get_nombre(self):
      return self.nombre
   
   def get_ruta(self): # Ruta formateada
      temp_ruta = ''
      for location in self.ruta:
         if temp_ruta == '':
               temp_ruta = temp_ruta + f'{location}'
         else:
               temp_ruta = temp_ruta + f' - {location}'
      return temp_ruta
   
   def get_fecha_salida(self): #Fecha formatada
      temp_fecha = self.fecha_salida.split('T', 1)[0].split('-', 2)
      year = temp_fecha[0]
      month = temp_fecha[1]
      day = temp_fecha[2]
      return f'{day}/{month}/{year}'

   def get_costo(self, tipo):
      if tipo == 'sencillo':
         return self.costo_boletos['simple']
      if tipo == 'premium':
         return self.costo_boletos['premium']
      if tipo == 'vip':
         return self.costo_boletos['vip']

   def get_capacidad(self, tipo):
      if tipo == 'sencillo':
         return self.capcaidad_habitaciones['simple']
      if tipo == 'premium':
         return self.capcaidad_habitaciones['premium']
      if tipo == 'vip':
         return self.capcaidad_habitaciones['vip']

   def agregar_piso(self, piso):
      self.pisos.append(piso)
   
   def update_habitaciones(self):
      with open('data_cruceros.txt', 'r') as data:
         for line in data:

            if self.nombre in line: # Encontrar line correspondiente con este crucero
               IDs = line.split('|')[1] # Contiene ids ([S{id}!])
               #print(f'Se a exitosamente actualizado {self.nombre}')
               for piso in self.pisos:
                  for habitacion in piso.habitaciones:
                     for letter in range(len(IDs)):
                        try:
                           substring = f'{IDs[letter]}{IDs[letter+1]}{IDs[letter+2]}' # El ID de habitacion
                           aux = f'{IDs[letter+3]}' # Este character determina si esta ocupado 
                           
                           if len(habitacion.get_id()) == 4: # Para no confundier SA1 con SA10
                              substring =f'{IDs[letter]}{IDs[letter+1]}{IDs[letter+2]}{IDs[letter+3]}'
                              aux = f'{IDs[letter+4]}'

                           
                           if substring == habitacion.get_id():
                              if aux == '!':
                                 habitacion.set_ocupado(False)
                                #print(f'{letter} ESTE ES EL AUX {aux} DE {habitacion.get_id()}')
                                 #print(f'{letter}:{IDs[letter]}{IDs[letter+1]}{IDs[letter+2]}')
                              elif aux == '@':
                                 habitacion.set_ocupado(True)
                              else:
                                 pass
                        except:
                           pass
      