# Importando archivos requeridos
from inicializacion import get_cruceros
from inicializacion import get_tours
from inicializacion import load_data
from inicializacion import get_restaurante
from menu import Menu as m

# Estos son los puntos de entrada para cada feature
from modulo1.representacion_cruceros import representar_cruceros
from modulo2.explorar_cruceros import explorar_cruceros
from modulo2.explorar_cruceros import explorar_cruceros_filtros
from modulo2.compra_habitaciones import elegir_habitacion
from modulo2.compra_habitaciones import comprar_habitacion
from modulo2.desocupar_habitacion import cancelar_reservacion
from modulo3.venta_tours import comprar_tour
from modulo4.gestionar_restaurante import buscar_item
from modulo4.gestionar_restaurante import gestion_productos
from modulo4.gestionar_restaurante import buscar_combo
from modulo5.estadisticas import selecionar_estadistica

def main():
   cruceros = get_cruceros() #Lista de todos los cruceros
   tours = get_tours() #Lista de todos los tours
   restaurante = get_restaurante()
   load_data(cruceros=cruceros) # Para mantener data de cruceros
   load_data(tours=tours) # Para mantener data de tours
   restaurante.update_menu() # Para mantenere data de restaurantes
   
   while True:
      opcion = m(['Gestión de Cruceros', 'Gestión de Habitaciones', 'Venta de tours', 'Gestión de restaurante', 'Estadísticas', 'Salir']).get_menu()

      if opcion == '1': # MODULO 1
         while True:
            opcion12 = m(['Explorar Todos los Cruceros', 'Volver']).get_menu()
            if opcion12 == '1': # Representacion de Cruceros (1)
               representar_cruceros(cruceros)
               break
            elif opcion12 == '2':
               break
            else:
               print('Opción elegida invalidad. Intentar otra vez.\n')
      elif opcion == '2': # MODULO 2
         while True:
            opcion21 = m(['Explorar Habitaciones' ,'Reservar Habitación', 'Cancelar Reservación', 'Volver']).get_menu()
            if opcion21 == '1': # Para Explorar habitaciones disponibles
               while True:
                  opcion22 = m(['Explorar todas las habitaciones dispobibles', 'Explorar Habitaciones por filtros', 'Volver']).get_menu()
                  if opcion22 == '1': # Explorar todas (1)
                     explorar_cruceros(cruceros)
                  elif opcion22 == '2': # Explorar con filtros (4)
                     explorar_cruceros_filtros(cruceros)
                  elif opcion22 == '3':
                     break
                  else:
                     print('Opción elegida invalidad. Intentar otra vez.\n')
            elif opcion21 == '2': # Para la compra de Habitacion (2)
               elegir_habitacion(cruceros)
            elif opcion21 == '3':
               cancelar_reservacion(cruceros)
            elif opcion21 == '4':
               break
            else:
               print('Opción elegida invalidad. Intentar otra vez.\n')
      elif opcion == '3': # MODULO 3
         comprar_tour(tours)
      elif opcion == '4': # MODULO 4
         while True:
            opcion41 = m(['Buscar item', 'Buscar Combo', 'Gestionar Items & Combos', 'Volver']).get_menu()
            if opcion41 == '1':
               buscar_item(restaurante)
            elif opcion41 == '2':
               buscar_combo(restaurante)
            elif opcion41 == '3':
               gestion_productos(restaurante)
            elif opcion41 == '4':
               break
            else:
               print('Opción elegida invalidad. Intentar otra vez.\n')
      elif opcion == '5': # MODULO 5
         selecionar_estadistica()
      elif opcion == '6':
         print('Programa terminado. Hasta luego!')
         break
      else:
         print('Opción elegida invalidad. Intentar otra vez.\n')
      

if __name__ == '__main__':
    main()