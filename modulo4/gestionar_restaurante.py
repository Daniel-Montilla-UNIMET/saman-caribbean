from menu import Menu as m
from inicializacion import update_menu_file

def update_datos(restaurante):
   update_menu_file(restaurante)
   print('Datos exitosamente guadados\n')

def agregar_item(restaurante):
   nombre = input('Ingrese nombre de item: ')
   opcion_tipo = m(['Alimento', 'Bebida']).get_menu()

   if opcion_tipo == '1':
      opcion_info = m(['Empaque', 'Preparación']).get_menu()
      tipo = 'a'
      if opcion_info == '1':
         info = 'e'
      elif opcion_info == '2':
         info = 'p'
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')
         return

   elif opcion_tipo == '2':
      opcion_info = m(['Pequeño', 'Mediano', 'Grande']).get_menu()
      tipo = 'b'
      if opcion_info == '1':
         info = 'p'
      elif opcion_info == '2':
         info = 'm'
      elif opcion_info == '2':
         info = 'g'
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')
         return
   
   else:
      print('Opción elegida invalidad. Intentar otra vez.\n')
      return
   
   try:
      precio = int(input('Ingrese precio de este item: '))
      if precio < 0:
         raise Exception
   except:
      print('Valor invalido. Intentar otravez')
      return

   restaurante.agregar_item(nombre, tipo, info, precio)
   update_datos(restaurante)

def agregar_combo(restaurante):
   nombre = input('Ingrese nombre de combo: ')
   opciones = [] # Indexs de todos los item selecionados
   items = []
   
   try:
      cantidad_items = int(input('Ingrese cantidad de items que quiere agregar (mas de 2): '))
      if cantidad_items < 2 or cantidad_items > len(restaurante.menu):
         raise Exception
   except:
      print('Opción elegida invalidad. Intentar otra vez.\n')
      return

   for item in restaurante.menu: # Para mostrar todos los items que se pudiera elegir
      items.append(f'{item.nombre} | {item.get_info()}, ${item.get_precio_base()}')

   for item in range(cantidad_items):
      print((f'\n    Item #{item+1} Escoga numero de item'))
      try:
         opcion = int(m(items).get_menu())
         if opcion > len(restaurante.menu) or opcion < 0:
            raise Exception
         opciones.append(opcion-1)
      except:
         print('Opción elegida invalidad. Intentar otra vez.\n')
         return
   
   try:
      precio = float(input('Ingrese precio de este combo: '))
      if precio < 0:
         raise Exception
   except:
      print('Valor invalido. Intentar otravez')
      return

   nombre_de_items = [] # Lista con todos los nombre del combo

   for index in range(len(opciones)):
      nombre_de_items.append(restaurante.menu[opciones[index]].nombre)

   restaurante.agregar_combo(nombre, precio, nombre_de_items)
   update_datos(restaurante)

def eliminar_item(restaurante):
   items = [] # Lista con todos los items del menu
   opciones = []
   print('\n     Items en menu que se pueden eliminar:')
   
   for item in restaurante.menu: 
      opciones.append(f'{item.nombre} | {item.get_info()}, ${item.get_precio_base()}')
      items.append(f'{item.nombre}')

   try:
      opcion = int(m(opciones).get_menu())
      if opcion > len(items) or opcion < 0:
         raise Exception
   except:
      print('Opción elegida invalidad. Intentar otra vez.\n')
      return

   restaurante.eliminar_item(opcion-1)
   update_datos(restaurante)

   return

def eliminar_combo(restaurante):
   combos = [] # Lista con todos los combos
   opciones = []
   if len(restaurante.combos) == 0:
      print('No hay combos para eliminar.')
   else:
      print('   Combos disponibles para eliminar:')

      for combo in restaurante.combos:
         opciones.append(f'{combo.nombre} ${combo.precio_base} | Items: {combo.items}')
         combos.append(f'{combo.nombre}')

      try:
         opcion = int(m(opciones).get_menu())
         if opcion > len(combos) or opcion < 0:
            raise Exception
      except:
         print('Opción elegida invalidad. Intentar otra vez.\n')
         return

      restaurante.eliminar_combo(opcion-1)
      update_datos(restaurante)

      return

def modificar_item(restaurante):
   items = [] # Lista con todos los items del menu
   opciones = []
   print('\n     Items en menu que se pueden modificar:')
   
   for item in restaurante.menu: 
      opciones.append(f'{item.nombre} | Tipo: {item.get_tipo()}, Info: {item.get_info()}, Precio: ${item.get_precio_base()}')
      items.append(f'{item.nombre}')

   try:
      opcion = int(m(opciones).get_menu())
      if opcion > len(items) or opcion < 0:
         raise Exception
   except:
      print('Opción elegida invalidad. Intentar otra vez.\n')
      return

   print('Que desea modificar de este item?')
   cosa_a_modificar = m(['Nombre', 'Tipo', 'Info', 'Precio']).get_menu()

   if cosa_a_modificar == '1':
      nombre = input('Ingrese nuevo nombre: ')
      restaurante.menu[opcion-1].modificar_algo('n', nombre)
   elif cosa_a_modificar == '2':
      print('Ingrese nuevo tipo: ')
      tipo = m(['Alimento', 'Bebida']).get_menu()
      if tipo == '1':
         new_tipo = 'a'
      elif tipo == '2':
         new_tipo = 'b'
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')
         return
      restaurante.menu[opcion-1].modificar_algo('t', new_tipo)
   elif cosa_a_modificar == '3':
      if restaurante.menu[opcion-1].tipo == 'a':
         info = m(['Empaque', 'Preparación']).get_menu()
         if info == '1':
            new_info = 'e'
         elif info == '2':
            new_info = 'p'
         else:
            print('Opción elegida invalidad. Intentar otra vez.\n')
            return
      elif restaurante.menu[opcion-1].tipo == 'b':
         info = m(['Pequeño', 'Mediano', 'Grande']).get_menu()
         if info == '1':
            new_info = 'p'
         elif info == '2':
            new_info = 'm'
         elif info == '3':
            new_info = 'g'
         else:
            print('Opción elegida invalidad. Intentar otra vez.\n')
            return
      restaurante.menu[opcion-1].modificar_algo('i', new_info)
   elif cosa_a_modificar == '4':
      try:
         new_price = float(input('Ingrese nuevo precio: '))
         if new_price < 0:
            raise Exception
      except:
         print('Opción elegida invalidad. Intentar otra vez.\n')
         return
      restaurante.menu[opcion-1].modificar_algo('p', new_price)
   else:
      print('Opción elegida invalidad. Intentar otra vez.\n')
      return

   update_datos(restaurante)
   return

def gestion_productos(restaurante):
   while True:
      b2 = m(['Agregar Item', 'Agregar Combo', 'Eliminar Item', 'Eliminar Combo', 'Modificar Item', 'Volver']).get_menu()

      if b2 == '1':
         agregar_item(restaurante)
      elif b2 == '2':
         agregar_combo(restaurante)
      elif b2 == '3':
         eliminar_item(restaurante)
      elif b2 == '4':
         eliminar_combo(restaurante)
      elif b2 == '5':
         modificar_item(restaurante)
      elif b2 == '6':
         break
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')

def mostrar_combo(combo):
   print(f'''   Nombre del Combo ➜ {combo.nombre}
   Item Incluidos ➜  {combo.items}
   Precio Base ➜  ${combo.precio_base}
   Precio Total ➜  ${combo.get_precio_total()}
   ''')

def mostrar_item(item):
   print(f'''   Nombre del item ➜  {item.nombre}
   Tipo ➜  {item.get_tipo()}
   Info ➜  {item.get_info()}
   Precio Base ➜  ${item.precio_base}
   Precio Total ➜  ${item.get_precio_total()}
   ''')

def buscar_combo(restaurante):
   b2 = m(['Buscar por nombre', 'Por precio', 'Ver Todos','Volver']).get_menu()

   if b2 == '1': # Por nombre
      nombre = input('Ingrese nombre: ')

      for combo in restaurante.combos:
         if combo.nombre == nombre:
            mostrar_combo(combo)
            return

   elif b2 == '2': # Por price range
      try:
         minimo = float(input('Ingrese precio minimo: '))
         maximo = float(input('Ingrese precio maximo: '))
      except:
         print('Opción elegida invalidad. Intentar otra vez.\n')
         return

      print(f'Todos los items entre ${minimo} y ${maximo}:')
      for combo in restaurante.combos:
         if combo.precio_base > minimo and combo.precio_base < maximo:
            mostrar_combo(combo)

   elif b2 == '3':
      for combo in restaurante.combos:
         mostrar_combo(combo)
   elif b2 == '4':
      return
   else:
      print('Opción elegida invalidad. Intentar otra vez.\n')

def buscar_item(restaurante):
   b1 = m(['Buscar por nombre', 'Por precio', 'Ver todos', 'Volver']).get_menu()

   if b1 == '1': # Por nombre
      nombre = input('Ingrese nombre: ')
      print('Productos que hacen match el nombre ingresado:\n')

      for item in restaurante.menu:
         if item.nombre == nombre:
            mostrar_item(item)
      

   elif b1 == '2': # Por price range
      try:
         minimo = float(input('Ingrese precio minimo: '))
         maximo = float(input('Ingrese precio maximo: '))
      except:
         print('Opción elegida invalidad. Intentar otra vez.\n')

      print(f'Todos los items entre ${minimo} y ${maximo}:\n')
      for item in restaurante.menu:
         if item.precio_base > minimo and item.precio_base < maximo:
            mostrar_item(item)

   elif b1 == '3':
      for item in restaurante.menu:
         mostrar_item(item)
   elif b1 == '4':
      return
   else:
      print('Opción elegida invalidad. Intentar otra vez.\n')
