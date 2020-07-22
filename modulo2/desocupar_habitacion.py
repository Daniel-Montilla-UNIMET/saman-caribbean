from menu import Menu as m
from modulo1.representacion_cruceros import representar_cruceros
from inicializacion import update_crucero_file

def update_datos(habitacion, cruceros):
   habitacion.set_ocupado(False) # Cambiando el state

   # Primero haces update el file con la data de los cruceros NOTA: Intente buscar una manera de buscar la linea con el nombre del crucero y replazar el ID de la habitacion. Lamentablemnete no encontre una solucion viable. Por ello estoy escribiendo todo el file cada vez
   update_crucero_file(cruceros)
   
      

def cancelar_reservacion(cruceros):
   while True:
      representar_cruceros(cruceros)
      try:
         c1 = int(input('Introduja numero de crucero: '))
         if c1 > len(cruceros):
            raise Exception

         piso = int(m(['Sencillo', 'Premium', 'VIP']).get_menu())
         if piso > 3:
            raise Exception

      except:
         print('Opción elegida invalidad. Intentar otra vez.\n')

      for crucero in range(len(cruceros)):
         if crucero == c1-1:
            print('\n Passillos ocupados: ')
            cruceros[crucero].pisos[piso - 1].get_representacion_ocupado()
            
            c2 = input('Ingrese ID (E.g. D3) de la habitacion que quiera desocupar: ')

            habitaciones_disponibles_id = [] # ID de habitaciones q esta ocupadas

            for habitacion in cruceros[crucero].pisos[piso - 1].habitaciones:
               if habitacion.ocupado == True:
                  habitacion_disponible = habitacion
                  habitaciones_disponibles_id.append(habitacion.identificador)

            if c2 in habitaciones_disponibles_id: # Chekeando que habitacion este disponible
               print('No refunds btw :)') # No estoy quitando los pagos que se hicieron para mantener los datos del cliente
               c3 = m([f'Confirmar Cancelacion de Habitacion {habitacion_disponible.get_id()}', 'No, Volver']).get_menu()
               if c3 == '1':
                  update_datos(habitacion_disponible, cruceros)
               else:
                  print('Cancelacion NO exitosa.')
                  return
            
            else:
               print('\n ID no disponible. Verifique datos.')
               pass

            return