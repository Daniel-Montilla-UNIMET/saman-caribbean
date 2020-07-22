# Importando archivos requeridos
from modulo1.representacion_cruceros import representar_cruceros
from menu import Menu as m

def mostrar_crucero(crucero, explore=True):
   while True:
      print(f'''
      Actualmente {'explorando' if explore else 'viendo'} pisos de {crucero.get_nombre()}!

               Capacidad    Costo    
   Sencillo:    {crucero.get_capacidad('sencillo')}            ${crucero.get_costo('sencillo')}    
    Premium:    {crucero.get_capacidad('premium')}            ${crucero.get_costo('premium')}    
        VIP:    {crucero.get_capacidad('vip')}            ${crucero.get_costo('vip')}    
      ''')

      print(f'Eliga piso que quisiera {"explorar" if explore else "ver"}')

      seleccion2 = m(['Sencillo', 'Premium', 'VIP']).get_menu()

      if seleccion2 == '1': # Sencillo
         crucero.pisos[int(seleccion2) - 1].get_representacion()
         return seleccion2
      elif seleccion2 == '2': # Premium
         crucero.pisos[int(seleccion2) - 1].get_representacion()
         return seleccion2
      elif seleccion2 == '3': # VIP
         crucero.pisos[int(seleccion2) - 1].get_representacion()
         return seleccion2
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')

def explorar_cruceros(cruceros):
   representar_cruceros(cruceros) # Mostrar cruceros actuales
   seleccion = input('Eliga el numero de crucero del cual quisiera explorar: ')

   for crucero in range(len(cruceros)):
      if seleccion == f'{crucero + 1}':
         mostrar_crucero(cruceros[crucero])
         return
   
   print('Opción elegida invalidad. Intentar otra vez.\n')

def mostrar_por_tipo(tipo, habitaciones):
   print(f'Todas las habitaciones de tipo {tipo}:\n')
   matching = [] # Lista con todas las habitaciones que cumplen criterio
   for habitacion in habitaciones:
      if habitacion.tipo == tipo:
         matching.append(habitacion)
   
   for habitacion in matching:
      print(f'Habitacion: {habitacion.identificador} | Capacidad: {habitacion.capacidad} | Ocupado?: {"Si" if habitacion.ocupado else "No"} | Tipo: {habitacion.tipo} | Pertenece: {habitacion.crucero_padre}')

def mostrar_por_capacidad(capacidad, habitaciones):
   print(f'Todas las habitaciones con capacidad {capacidad}:\n')
   matching =[] # Lista con todas las habitaciones que cumplen criterio
   for habitacion in habitaciones:
      if habitacion.capacidad == capacidad:
         matching.append(habitacion)
      
   if len(matching) == 0:
      print('Ningun resultado encontrado. Verifique sus datos\n')
   else:
      for habitacion in matching:
         print(f'Habitacion: {habitacion.identificador} | Capacidad: {habitacion.capacidad} | Ocupado?: {"Si" if habitacion.ocupado else "No"} | Tipo: {habitacion.tipo} | Pertenece: {habitacion.crucero_padre}')

def mostrar_por_identidicador(tipo, identificador, habitaciones):
   print(f'Todas las habitaciones de tipo {tipo} y identificador {identificador}\n')
   matching = []
   for habitacion in habitaciones:
      if habitacion.tipo == tipo and habitacion.identificador == identificador:
         matching.append(habitacion)
   
   if len(matching) == 0:
      print('Ningun resultado encontrado. Verifique sus datos\n')
   else:
      for habitacion in matching:
         print(f'Habitacion: {habitacion.identificador} | Capacidad: {habitacion.capacidad} | Ocupado?: {"Si" if habitacion.ocupado else "No"} | Tipo: {habitacion.tipo} | Pertenece: {habitacion.crucero_padre}')

def explorar_cruceros_filtros(cruceros):
   print('  Que tipo de filtro le quiere aplicar a la busqueda?')
   
   all_habitaciones = [] # Todos los objetos de habitaciones en un solo lugar
   for crucero in cruceros: 
      for piso in crucero.pisos:
         for habitacion in piso.habitaciones:
            all_habitaciones.append(habitacion)
            habitacion.add_parent_crucero(crucero.get_nombre()) # Agregando referecia al crucero padre

   while True:
      filtro = m(['Por Tipo', 'Por Capacidad', 'Por ID', 'Volver']).get_menu()
      
      if filtro == '1': # Por tipo
         tipo = m(['Sencilla', 'Premium', 'VIP', 'Volver']).get_menu()

         if tipo == '1':
            mostrar_por_tipo('simple', all_habitaciones)
         elif tipo == '2':
            mostrar_por_tipo('premium', all_habitaciones)
         elif tipo == '3':
            mostrar_por_tipo('vip', all_habitaciones)
         elif tipo == '4':
            pass
         else: 
            print('Opción elegida invalidad. Intentar otra vez.\n')

      elif filtro == '2': # Por Capcidad
         while True:
            try:
               capacidad = int(input('Ingrese capacidad de habitacion: '))
               break
            except:
               print('Valor ingresado invalido. Intentar otra vez.\n')
         mostrar_por_capacidad(capacidad, all_habitaciones)

      elif filtro == '3': # Por ID (Tipo, Pasillo, Habitacion_num)
         print('     Primero escoja el tipo de habitacion')
         tipo = m(['Sencilla', 'Premium', 'VIP', 'Volver']).get_menu()
         identificador = input('Ingrese identificador (E.g: C3): ')
         
         if tipo == '1':
            mostrar_por_identidicador('simple', identificador, all_habitaciones)
         elif tipo == '2':
            mostrar_por_identidicador('premium', identificador, all_habitaciones)
         elif tipo == '3':
            mostrar_por_identidicador('vip', identificador, all_habitaciones)
         elif tipo == '4':
            pass
         else: 
            print('Opción elegida invalidad. Intentar otra vez.\n')
   
      elif filtro == '4':
         break
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')

   