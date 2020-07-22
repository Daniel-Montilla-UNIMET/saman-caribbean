from menu import Menu as m

# NOTA: Este modulo trabja mayormente con el file: cuentas.txt

def todos_los_clientes(): # Imprime todos los clientes y tambien retorna lista con cedulas
   clientes = [] # [{cedula: int, pagos_total: $int, pagos_cantidad: int, tour: bool, crucero: bool}, {...}, ...]
   with open('cuentas.txt', 'r') as data:
      for line in data:
         add_new = True
         cedula = int(line.split('>')[0]) # int
         pago = float(line.split('|')[1]) # Float
         identidicador = line.split('>')[1][0] # El primer caractes del split 'b' o 't'

         for cliente in range(len(clientes)): # Check si existe el cliente
            if cedula == clientes[cliente]['Cedula']:
               add_new = False
               index = cliente
         
         if add_new: # Si no existe

            if identidicador == 'b': # Verificando cual tipo de compra es
               crucero = True
               tour = False
            if identidicador == 't':
               tour = True
               crucero = False

            clientes.append({'Cedula': cedula, 'pagos_total': pago, 'pagos_cantidad': 1, 'tour': tour, 'crucero': crucero})
         elif add_new == False: # Si existe, buscar el item y cambiarlo
            
            if identidicador == 'b': # Verificando cual tipo de compra es
               clientes[index]['crucero'] = True

            if identidicador == 't':
               clientes[index]['tour'] = True
            
            clientes[index]['pagos_total'] += pago
            clientes[index]['pagos_cantidad'] += 1
            

   return clientes

def todos_los_cruceros():
   cruceros = [] # [{crucero_name: str, tickets: int}, {...}, ...]
   with open('cuentas.txt', 'r') as data:
      for line in data:
         add_new = True
         if line.split('>')[1][0] == 'b': # Si el identificador es del crucero
            crucero_name = line.split('>')[1].split('|')[0][1:] # str del nombre de crucero
            for crucero in range(len(cruceros)): # Check si existe el cliente
               if crucero_name == cruceros[crucero]['Crucero_name']:
                  add_new = False
                  index = crucero
            
            if add_new: # Si no existe
               cruceros.append({'Crucero_name': crucero_name, 'tickets': 1})
            elif add_new == False: # Si existe, buscar el item y cambiarlo
               cruceros[index]['tickets'] += 1

   return cruceros

def promedio_de_gastos():
   facturas = [] # Lista con todos los valore numericos de los gastos

   with open('cuentas.txt', 'r') as data:
      for line in data:
         try:
            gasto = line.split('|')[1]
            facturas.append(float(gasto)) # Apendiar gasto
         except:
            pass

   if len(facturas) == 0:
      print('No hay ningun pago. Agregar pagos!')
      return
   else:
      suma = 0
      cantidad = len(facturas)

      for i in range(len(facturas)):
         suma += facturas[i]
      
      promedio = suma/cantidad

      print(f'''
   Promedio de pago (ticket + tour): {promedio}
   Cantidad de pagos: {cantidad}
      ''')

def promedio_de_gastos_cliente():
   clientes = todos_los_clientes() # Array que tiene todos los clientes
   print('\n Lista de todos los clientes: ')
   for cliente in range(len(clientes)):
      print(f'[{cliente+1}] {clientes[cliente]["Cedula"]}')
   
   r1 = int(input('Ingrese numero de cliente para ver su promedio: ')) - 1
   
   try:
      if r1 in range(len(clientes)):
         print(f'''
         Datos de cliente {clientes[r1]['Cedula']}
   Gastos totales: ${clientes[r1]['pagos_total']}
   Cantidad de pagos: {clientes[r1]['pagos_cantidad']}
   Promedio de gastos: {clientes[r1]['pagos_total']/clientes[r1]['pagos_cantidad']}
   ''')
      else:
         raise Exception
   except:
      print('Opción elegida invalidad. Intentar otra vez.\n')

def porcentaje_de_no_tours():
   clientes = todos_los_clientes()
   
   clientes_sin_tour = 0
   clientes_totales = len(clientes)

   for cliente in clientes:
      if cliente['tour'] == False:
         clientes_sin_tour += 1

   
   porcentaje = (clientes_sin_tour)/(clientes_totales)*(100)
   
   print(f'       Porncentaje de clientes que NO compran tour: %{porcentaje}')

def top3_clientes():
   clientes = todos_los_clientes() # Todos los clientes en orden de pago total

   for i in range(len(clientes)-1, 0, -1): # Bubble Sort porque es el mas facil de implementar 
      for j in range(i):
         if clientes[j]['pagos_total'] > clientes[j+1]['pagos_total']:
            aux = clientes[j]
            clientes[j] = clientes[j+1]
            clientes[j+1] = aux
   
   top3 = []
   
   for cliente in range(len(clientes), len(clientes)-3, -1): # sacar los top 3
      top3.append(clientes[cliente-1])

   for cliente in range(len(top3)): # Imprimirlos
      print(f'    {cliente+1}.  Cliente: {top3[cliente]["Cedula"]}, Pagos Totals: {top3[cliente]["pagos_total"]}')
   print('\n')

def top3_cruceros():
   cruceros = todos_los_cruceros()

   for i in range(len(cruceros)-1, 0, -1): # Bubble Sort porque es el mas facil de implementar 
      for j in range(i):
         if cruceros[j]['tickets'] > cruceros[j+1]['tickets']:
            aux = cruceros[j]
            cruceros[j] = cruceros[j+1]
            cruceros[j+1] = aux 
   
   top3 = []
   
   for crucero in range(len(cruceros), len(cruceros)-3, -1): # sacar los top 3
      top3.append(cruceros[crucero-1])

   for crucero in range(len(top3)): # Imprimirlos
      print(f'    {crucero+1}.  Crucero: {top3[crucero]["Crucero_name"]}, Tickets: {top3[crucero]["tickets"]}')
   print('\n')
   
def selecionar_estadistica():
   while True:
      estadistica = m(['Promedio de gastos de todos los clientes', 'Promedio de gastos de un solo cliente','Porcentaje de clientes que no comprar tour', 'Top 3 Clientes', 'Top 3 Cruceros con mayor venta de tickets', 'Volver']).get_menu()
      try:
         if estadistica == '1': # NO lei bien las isntrucciones. Pero bueno dejo esto aqui!
            promedio_de_gastos()
         elif estadistica == '2':
            promedio_de_gastos_cliente()
         elif estadistica == '3':
            porcentaje_de_no_tours()
         elif estadistica == '4':
            top3_clientes()
         elif estadistica == '5':
            top3_cruceros()
         elif estadistica == '6':
            break
         else:
            print('Opción elegida invalidad. Intentar otra vez.\n')
      except:
         print('Todavia no hay pagos. Realize almenos un pago para utilizar este modulo')
         break