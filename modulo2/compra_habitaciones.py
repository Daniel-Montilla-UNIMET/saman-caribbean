# Importando archivos requeridos
from menu import Menu as m
from modulo1.representacion_cruceros import representar_cruceros
from math import floor
from objetos.persona import Persona
from inicializacion import update_crucero_file

def update_datos(habitacion, income, persona, cruceros):
   habitacion.set_ocupado(True) # Cambiando el state

   # Primero haces update el file con la data de los cruceros NOTA: Intente buscar una manera de buscar la linea con el nombre del crucero y replazar el ID de la habitacion. Lamentablemnete no encontre una solucion viable. Por ello estoy escribiendo todo el file cada vez
   update_crucero_file(cruceros)
   
   # Ahora creamos un archivo que maneje todoa las cuentas (para modulo de estadisticas)
   try: # Intentar crear archivo, si no puede apendiar
      with open('cuentas.txt', 'x') as data:
         data.write(f'{persona.cedula}>b{habitacion.crucero_padre}|{income}\n')#client>ticketNOMBRECRUCERO|$
   except:
      factura = f'{persona.cedula}>b{habitacion.crucero_padre}|{income}\n'
      enter = True
      with open('cuentas.txt', 'r') as data:
         for line in data:
            if line == factura:
               enter = False
      if enter:
         with open('cuentas.txt', 'a') as data:
            data.write(factura)

def mostrar_factura(current_cart):
   print('\nTodos los datos exitosamente ingresados!. Su factura: (Se tarda un rato!)')
   
   # Formatiando datos para visibilidad en factura
   cantidad_boletos = len(current_cart)
   habitaciones = ''
   for persona in current_cart: # Agregando todas las habitaciones selecionadas
      if persona.habitacion not in habitaciones:
         habitaciones = habitaciones + f'{persona.habitacion} '
   sub_total = 0
   for persona in current_cart:
      sub_total += persona.get_costo_boleto()[0]
   impuesto = 0.16

   total = sub_total + sub_total*impuesto

   print(
   f'''
   Cantidad de Boletos: {cantidad_boletos}
   Habitacion(es): {habitaciones}
      Resumen de cada boleto:''')

   for boleto in current_cart:
      descuentos = boleto.get_costo_boleto()[1]
      if len(descuentos) > 0:
         print(f'\n       ⇃Descuento(s) para el boleto de {boleto.nombre}⇂')
         for descuento in range(len(descuentos)):
            print(f'''        {descuento+1}. {descuentos[descuento]}''')
   
   print(
   f'''
   Total: ${total}
   ''')

   return total

def comprar_habitacion(habitacion, personas, cruceros):
   print('\nA continuacion se le preguntara informacion necesaria para completar la compra.')
   current_cart = [] # Lista de objetos personas en la cuenta actual

   while True:
      if len(current_cart) < personas: # Asegurar que la cantidad de personas que se registran coinciden con la cantidad del party
         try:
            if len(current_cart) == 0:
               print(f'\n⇃Datos de persona a pagar! (La compra estara a su nombre)')
            else:
               print(f'\n⇃Datos de persona #{len(current_cart) + 1}⇂')

            nombre = input('Ingrese su nombre: ')
            cedula = int(input('Ingerese su cedula: '))
            edad = int(input('Ingrese su edad: '))
            discapacidad = input('Sufre de alguna discapacidad? [Y/N]: ')

            if cedula < 0: # Para que gente no ponga numeros negativos
               raise Exception

            # Verificando que el input es Y o N. Y formatiando el valor para que sea bool
            if discapacidad == 'y' or discapacidad == 'Y':
               discapacidadF = True
            elif discapacidad == 'n' or discapacidad == 'N':
               discapacidadF = False
            else:
               raise Exception
            
            temp_persona = Persona( # Creando objeto persona
               nombre,
               cedula,
               edad,
               discapacidadF,
               habitacion.identificador,
               habitacion.costo
            )
            
            print(f'{temp_persona.nombre} se ha Registrado!') # Verificando Registracion
            current_cart.append(temp_persona)
            habitacion.agregar_personas(temp_persona) # porsicaso necesito una referencio luego
         except:
            print('Valor invalido. Intente otravez.')
      else: # Una vez que la cantidad de personas correctas se registren, salir del loop
         break
   
   # Una vez que se registraron todos. Mostramos factura y preguntamos si la compra se quire hacer para finalizar transaccion
   costo = mostrar_factura(current_cart)
   while True:
      print('Confirma tu compra')
      confirmar = m(['Si', 'Cancelar']).get_menu()

      if confirmar == '1':
         print('Tu Compra ha sido realizada!')
         update_datos(habitacion, costo, current_cart[0], cruceros)
         break
      elif confirmar == '2':
         print('Compra Cancelada')
         break
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')

def comprar_habitaciones(habitaciones, personas, cruceros):
   print('\nA continuacion se le preguntara informacion necesaria para completar la compra.')
   current_cart = [] # Lista de objetos personas en la cuenta actual

   while True:
      if len(current_cart) < personas: # Asegurar que la cantidad de personas que se registran coinciden con la cantidad del party
         try:
            if len(current_cart) == 0:
               print(f'\n⇃Datos de persona a pagar! (La compra estara a su nombre)')
            else:
               print(f'\n⇃Datos de persona #{len(current_cart) + 1}⇂')

            nombre = input('Ingrese su nombre: ')
            cedula = int(input('Ingerese su cedula: '))
            edad = int(input('Ingrese su edad: '))
            discapacidad = input('Sufre de alguna discapacidad? [Y/N]: ')

            # Verificando que el input es Y o N. Y formatiando el valor para que sea bool
            if discapacidad == 'y' or discapacidad == 'Y':
               discapacidadF = True
            elif discapacidad == 'n' or discapacidad == 'N':
               discapacidadF = False
            else:
               raise Exception
            
            temp_persona = Persona( # Creando objeto persona
               nombre,
               cedula,
               edad,
               discapacidadF,
               habitaciones[0].identificador,
               habitaciones[0].costo
            )
            
            print(f'{temp_persona.nombre} se ha Registrado!') # Verificando Registracion
            current_cart.append(temp_persona)
            habitaciones[0].agregar_personas(temp_persona) # porsicaso necesito una referencio luego
         except:
            print('Valor invalido. Intente otravez.')
      else: # Una vez que la cantidad de personas correctas se registren, salir del loop
         break
   
   # Una vez que se registraron todos. Mostramos factura y preguntamos si la compra se quire hacer para finalizar transaccion
   costo = mostrar_factura(current_cart)
   while True:
      print('Confirma tu compra')
      confirmar = m(['Si', 'Cancelar']).get_menu()

      if confirmar == '1':
         print('Tu Compra ha sido realizada!')
         for habitacion in range(len(habitaciones)):
            update_datos(habitaciones[habitacion], costo, current_cart[0], cruceros)
         break
      elif confirmar == '2':
         print('Compra Cancelada')
         break
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')

def seleccionar_habitacion(piso, personas, cruceros, compras=1):
   habitaciones_disponibles = []

   for habitacion in piso.habitaciones:
      if habitacion.ocupado == False:
         habitaciones_disponibles.append(habitacion)

   if compras > 1: # Si la cantidad de habitaciones a comprar es mas de 1
      while True:
         print('Habitaciones disponibles para su viaje: ')
         piso.get_representacion()

         habitaciones_a_comprar = [] # Seleccion multiple de habitaciones

         for habitacion_num in range(compras): # Agregando habitaciones que quiere el cliente
            choice = input(f'Eliga el ID de habitacion #{habitacion_num + 1} (E.g.: 2F) que quiere comprar: ')
            habitaciones_a_comprar.append(choice)

         habitaciones = []
         for habitacion in habitaciones_disponibles: # Verificando que input es valido
            for habitacion_a_comprar in habitaciones_a_comprar:
               if habitacion_a_comprar == habitacion.identificador:
                  habitaciones.append(habitacion)

         if len(habitaciones) == len(habitaciones_a_comprar): # Si es valido:
            comprar_habitaciones(habitaciones, personas, cruceros)
            return
         else:
            print('Algun ID invalido, Intente otravez\n')

   else: # Si la cantidad de habitaciones a comprar es exactamente 1
      print('Habitaciones disponibles para su viaje: ')
      piso.get_representacion()
      option = input('Eliga el ID de habitacion (E.g.: 4C) que quiere comprar: ')
      for habitacion in habitaciones_disponibles:
         if option == habitacion.identificador:
            comprar_habitacion(habitacion, personas, cruceros)
            return
      print('Opción elegida invalidad. Intentar otra vez.\n')

def comprar_por_criterios(crucero, cruceros):
   print('\n   Escoga tipo de habitacion')
   try:
      piso = int(m(['Sencillo', 'Premium', 'VIP']).get_menu()) - 1
      party = int(input('Cantidad de personas en su party: '))

      if crucero.pisos[piso].capacidad_habitacion < party: # Determinando Cantidadd de habitaciones que se deben comprar si la party es mayor que la capacidad
         habitaciones_a_compar = floor((party)/(crucero.pisos[piso].capacidad_habitacion))
         if party % crucero.pisos[piso].capacidad_habitacion != 0:
            habitaciones_a_compar += 1
         print(f'La cantidad de gente que viaja con usted es mayor que la cantidad de gente que puede viajar en habitaciones de este tipo. Por lo tanto, debe comprar un minimo de {habitaciones_a_compar} habitaciones.')

         seleccionar_habitacion(crucero.pisos[piso], party, cruceros, habitaciones_a_compar)
      else: # Si la cantidad de habitaciones a comprar es solamente 1
         seleccionar_habitacion(crucero.pisos[piso], party, cruceros)
   except:
      print('Introdujo un valor invalido. Intentelo denuevo\n')

def elegir_habitacion(cruceros):
   while True:
      o1 = m(['Comprar en base a destino', 'Comprar en base a crucero', 'Volver']).get_menu()
      if o1 == '1': #En base a destino
         destinos_disponibles = [] # Lista con destinos disponibles
         for crucero in cruceros:
            for destino in crucero.ruta:
               if destino not in destinos_disponibles:
                  destinos_disponibles.append(destino)
            
         print(f'Destinos disponibles: \n')
         for destino in range(len(destinos_disponibles)):
            print(f'    [{destino+1}] {destinos_disponibles[destino]}')
   
         o2 = input('\nEscoja Cual destino quiera: ')
         o22 = None
         for i in range(len(destinos_disponibles)):
            if o2 == f'{i+1}':
               o22 = destinos_disponibles[i]
         
         if o22 == None: # Si es invalida devolver
            print('Opción elegida invalidad. Intentar otra vez.\n')
            break
         
         cruceros_disponibles = [] # Todos los cruseros con el destino requerido

         for crucero in cruceros:
            for destino in crucero.ruta:
               if o22 in destino:
                  if crucero.get_nombre() not in cruceros_disponibles: # Cunado una ruta esa dos veces
                     cruceros_disponibles.append(crucero.get_nombre())
         
         print(f'Los crucero con ese destino son: {cruceros_disponibles}\n')
         
         representar_cruceros(cruceros) # Mostrar cruceros actuales
         barco = input(f'NOTA! El(los) unico(s) crucero(s) con su destino querido es(son): {cruceros_disponibles}\nEliga el numero de crucero del cual quiera comprar una habitacion: ')

         for crucero in range(len(cruceros)):
            if barco == f'{crucero + 1}':
               comprar_por_criterios(cruceros[crucero], cruceros)
               return

         print('Opción elegida invalidad. Intentar otra vez.\n')

      elif o1 == '2': # En base a barco
         while True:
            representar_cruceros(cruceros) # Mostrar cruceros actuales
            barco = input('Eliga el numero de crucero del cual quiera comprar una habitacion: ')

            for crucero in range(len(cruceros)):
               if barco == f'{crucero + 1}':
                  comprar_por_criterios(cruceros[crucero], cruceros)
                  return

            print('Opción elegida invalidad. Intentar otra vez.\n')

      elif o1 == '3':
         break
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')