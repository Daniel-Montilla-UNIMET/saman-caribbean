# Importando Objectos
from objetos.crucero import Crucero
from objetos.piso import Piso
from objetos.habitacion import Habitacion
from objetos.tours import Tour
from objetos.restaurante import Restaurante

# Importando Librerias requeridas
import requests
from string import ascii_uppercase

def update_crucero_file(cruceros):
   with open('data_cruceros.txt', 'w') as data: # Re escribiendo todo el file
      for crucero in cruceros:
         data.write(f'{crucero.nombre}|')
         for piso in crucero.pisos:
            for habitacion in piso.habitaciones:
               if habitacion.ocupado: # Si esta ocupado
                  data.write(f'{habitacion.get_id()}@')
               else: # Si no esta ocupado
                  data.write(f'{habitacion.get_id()}!')
         data.write('\n')

def update_menu_file(restaurante):
   # Para items --> NOMBRE>tipo>INFO|precio
      # Nombre: str
      # Tipo: 'a'=alimento o 'b'=bebida
      # Info: bebida('p'=pequeno 'm'=mediano 'g'=grande) alimento('p'=preparación 'e'=empaque)
      # Precio: Float
   
   # Para combos --> NOMBRE>item1name, item2name,...|precio
      # Nombre: str
      # Tipo: 'a'=alimento o 'b'=bebida
      # Precio: Float

   with open('data_menu.txt', 'w') as data:
         for item in restaurante.menu:
            data.write(f'{item.nombre}>{item.tipo}>{item.info}|{item.precio_base}\n')
         for combo in restaurante.combos:
            items = '' # Contiene todos los items de manera formatada
            for item in combo.items:
               items += f'{item},'
            data.write(f'{combo.nombre}>{items}|{combo.precio_base}\n')

def update_tour_file(tours):
   with open('data_tours.txt', 'w') as data:
      for tour in tours:
         data.write(f'{tour.nombre}|{tour.cupos_ocupados}\n')

# Este archivo manegara la llamada al API y la creacion de todos los objetos necesarios
def get_cruceros():
   
   cruceros = [] #Lista de todos los cruceros
   data = requests.request("GET", "https://saman-caribbean.vercel.app/api/cruise-ships").json() # API request

   for crucero in range(len(data)): # Agregando Objetos de cruceros
      name = data[crucero]['name']
      if data[crucero]['name'] == 'El Libertador del Océano': # Porque é es incompatible
         name = 'El Libertador del Oceano'
      
      cruceros.append(Crucero(
         name,        # Str
         data[crucero]['route'],       # Arr
         data[crucero]['departure'],   # Str
         data[crucero]['cost'],        # Dict
         data[crucero]['rooms'],       # Dict
         data[crucero]['capacity']     # Dict
      ))
   
   def agregar_pisos(crucero): # Formatiando informacion del request para manejo mas facil. 
      pisos = list(crucero.alojamiento.keys())
      pasillos = [arr[0] for arr in list(crucero.alojamiento.values())]
      habitaciones = [arr[1] for arr in list(crucero.alojamiento.values())]
      capacidades = [x for x in list(crucero.capcaidad_habitaciones.values())]
      costos = [x for x in list(crucero.costo_boletos.values())]
      for piso in range(len(pisos)):
         crucero.agregar_piso(Piso(
            pisos[piso],
            pasillos[piso],
            habitaciones[piso],
            capacidades[piso],
            costos[piso],
            crucero.get_nombre()
         ))
   
   def agregar_habitaciones(piso):
         # Matrix pasillos x habitaciones
      letras = list(ascii_uppercase) # lista en orden de UPPERCASE alfabeto
      for pasillo in range(piso.num_pasillos):
         for habitacion in range(piso.num_habitaciones):
            piso.agregar_habitacion(Habitacion(
               letras[pasillo] + str(habitacion+ 1), # Identificador
               piso.capacidad_habitacion,
               piso.nivel,
               piso.costo_habitacion,
               piso.crucero_padre
            ))


   for crucero in range(len(cruceros)): # Agregando Objectos de piso a los cruceros
      agregar_pisos(cruceros[crucero])
      for piso in range(len(cruceros[crucero].pisos)): # Agregando Objectos de habitacion a los pisos
         agregar_habitaciones(cruceros[crucero].pisos[piso])

   try: 
      with open('data_cruceros.txt', 'x') as data: # Creando y agregando informacion si el archivo data, no esta creado
         for crucero in cruceros:
            data.write(f'{crucero.nombre}|')
            for piso in crucero.pisos:
               for habitacion in piso.habitaciones:
                  if habitacion.ocupado: # Si esta ocupado
                     data.write(f'{habitacion.get_id()}@')
                  else: # Si no esta ocupado
                     data.write(f'{habitacion.get_id()}!')
            data.write('\n')
   except:
      pass

   return cruceros

def get_tours():
   tours = [] # Lista con todos los objetos tour
   
   # Agregando tours
   tours.append(Tour('Tour en el puerto', 30, 4, '7 A.M', 10, '10% a partir de la tercera persona'))
   tours.append(Tour('Degustacion de comida local', 100, 2, '12 P.M', 100))
   tours.append(Tour('Trotar por el pueblo/ciudad', 0, 1000, '6 A.M', 9999999))
   tours.append(Tour('Visita a lugares historicos', 40, 4, '10 A.M', 15, '10% a partir de la tercera persona'))

   try: 
      with open('data_tours.txt', 'x') as data: # Creando y agregando informacion si el archivo tours_data, no esta creado
         for tour in tours:
            data.write(f'{tour.nombre}|{tour.cupos_ocupados}\n')
   except:
      pass

   return tours

def get_restaurante():
   restaurante = Restaurante()

   # Generar algunas comidas y bebidas
   restaurante.agregar_item('Haburgesa', 'a', 'e', 10)
   restaurante.agregar_item('Perro Caliente', 'a', 'p', 7)
   restaurante.agregar_item('CocaCola', 'b', 'p', 3)
   restaurante.agregar_item('Pepsi', 'b', 'm', 4)
   restaurante.agregar_item('Malta', 'b', 'g', 5)
   restaurante.agregar_item('Huevo frito', 'a', 'p', 3)
   restaurante.agregar_item('Tocino frito', 'a', 'p', 3)
   restaurante.agregar_item('Vaso de Agua', 'b', 'p', 3)
   restaurante.agregar_combo('Desayuno Americano', 17, ['Huevo frito', 'Tocino frito', 'CocaCola'])

   # Para items --> NOMBRE>tipo>INFO>precio
      # Nombre: str
      # Tipo: 'a'=alimento o 'b'=bebida
      # Info: bebida('p'=pequeno 'm'=mediano 'g'=grande) alimento('p'=preparación 'e'=empaque)
      # Precio: Float
   
   # Para combos --> NOMBRE>item1name, item2name,...>precio
      # Nombre: str
      # Tipo: 'a'=alimento o 'b'=bebida
      # Precio: Float
   
   try: #Creando archivo si no esta creado todavia
      with open('data_menu.txt', 'x') as data:
         for item in restaurante.menu:
            data.write(f'{item.nombre}>{item.tipo}>{item.info}|{item.precio_base}\n')
         for combo in restaurante.combos:
            items = '' # Contiene todos los items de manera formatada
            for item in combo.items:
               items += f'{item},'
            data.write(f'{combo.nombre}>{items}|{combo.precio_base}\n')
   except:
      pass

   return restaurante

def load_data(cruceros=[], tours=[], restaurante=None):
   for crucero in cruceros:
      crucero.update_habitaciones() # Hace mathc todos los datos del TXT al los objetos respectivos
   
   for tour in tours :
      tour.update_tour()
