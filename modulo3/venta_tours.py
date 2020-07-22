# Importando archivos requeridos
from menu import Menu as m
from inicializacion import update_tour_file

def update_datos(tour, party, cedula, tours): # NOTA: EN LAS INSTRUCCIONES NO DICE QUE SE LE AGREGE EL IMPUESTO POR LO TANTO NO LOS CONSIDERE AQUI EN TOURS
   # Primero agregamos el de update la cantidad de cupos
   tour.ocupar_cupos(party)

   update_tour_file(tours)

   # Ahora creamos un archivo que maneje todoa las cuentas (para modulo de estadisticas)
   try: # Intentar de crear archivo, si no puede apendiar
      with open('cuentas.txt', 'x') as data:
         data.write(f'{cedula}>t{tour.nombre}|{tour.get_costo(party)}\n')#client>ticketNOMBRECRUCERO|$
   except:
      factura = f'{cedula}>t{tour.nombre}|{tour.get_costo(party)}\n'
      enter = True
      with open('cuentas.txt', 'r') as data:
         for line in data:
            if line == factura:
               enter = False
      if enter:
         with open('cuentas.txt', 'a') as data:
            data.write(factura)
   print('        Compra exitosamente procesada!\n')

def mostrar_factura(cedula, party, tour):
   print(f'''  Factura
   Cedula de comprador: {cedula}
   Tour a comprar: {tour.nombre}
   Cantidad de Personas: {party}
   Tiempo de salida: {tour.tiempo}
   Costo total: ${tour.get_costo(party)}
   ''')

def representar_tours(tours):
   for tour in range(len(tours)):  # Imprime toda la info de cada objeto
      print(
   f"""        ✦ Tour #{tour + 1}
   Nombre de tour ➜  {tours[tour].nombre}
   Precio ➜  ${tours[tour].precio}/por persona
   Tiempo ➜  {tours[tour].tiempo}
   Descuento ➜  {tours[tour].descuentos}
   Maximas persona ➜  {tours[tour].get_max_persona()}
   Cupos disponibles ➜  {tours[tour].get_cupos_disponibles()}
   """)

def comprar_tour(tours):
   tours_disponibles = [] # Tours que todavia tienen cupo
   
   for tour in tours:
      if tour.get_disponibilidad():
         tours_disponibles.append(tour)

   while True:
      print('Estos son los tours disponibles\n')

      representar_tours(tours_disponibles)

      for tour in range(len(tours_disponibles)):
         print(f'    [{tour+1}] {tours_disponibles[tour].nombre}')
      
      oo1 = input('\nEscoja: ')
      
      opcion_tour = None
      
      for i in range(len(tours_disponibles)):
         if oo1 == f'{i+1}':
            opcion_tour = tours_disponibles[i]

      if opcion_tour == None: # Si es invalida devolver
         print('Opción elegida invalidad. Intentar otra vez.\n')
         break

      try:
         cedula = int(input('Ingrese su cedula: '))
         party = int(input('Numero de personas con usted: '))

         if party > opcion_tour.max_personas:
            print('Cantidad de personas en el party exede la cantidad de personas maximas')
            break

         if party + opcion_tour.cupos_ocupados > opcion_tour.cupos: # Asegurando que existen suficientes cupos
            print('\nCupos agotados. Si quiere este tour debe ingresar con menos personas.\n')
            break
         mostrar_factura(cedula, party, opcion_tour)
         
         print('Quiere comprar este tour?')
         confirmar = m(['Si', 'No']).get_menu()

         if confirmar == '1':
            update_datos(opcion_tour, party, cedula, tours)
            break
         elif confirmar == '2':
            break
         else:
            print('\nValor ingresado invalido. Intentar otra vez.')

      except:
         print('\nValor ingresado invalido. Intentar otra vez.')
      
      break