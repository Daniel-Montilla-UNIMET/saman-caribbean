from objetos.item import Item
from objetos.combo import Combo
from menu import Menu as m

class Restaurante:
   def __init__(self):
      self.menu = [] # Contiene items del restourante
      self.combos = [] # Contiene lista de item del restaurantes

   def agregar_item(self, nombre, tipo, info, precio):         
      n = nombre
      t = tipo
      i = info

      for item in self.menu: # Checkear que no se repita item
         if item.nombre == n and t == item.tipo and i == item.info:
            print(f'Item {item.nombre} no se pudo agregar porque ya existe este item\n')
            return

      self.menu.append(Item(
         n,
         t,
         i,
         precio
      ))
   
   def eliminar_item(self, index):
      try:
         self.menu.pop(index)
      except:
         print('Ocurrio un error. No se pudo eliminar item')

   def eliminar_combo(self, index):
      try:
         self.combos.pop(index)
      except:
         print('Ocurrio un error. No se pudo eliminar combo')

   def modificar_item(self, nombre_de_item, atributo, valor):
      for item in self.menu:
         if item.nombre == nombre_de_item:
            pass #TODO
      
      print(f'{nombre_de_item} no esta en este menu')
      return

   def update_menu(self):
      with open('data_menu.txt', 'r') as data:
         for line in data:
            nombre = line.split('>')[0]

            for item in self.menu: # Si es un item
               if item.nombre == nombre:
                  tipo = line.split('>')[1][0]
                  info = line.split('>')[2][0]
                  precio = float(line.split('|')[1])

                  item.tipo = tipo
                  item.info = info
                  item.precio_base = precio

            for combo in self.combos:
               if combo.nombre == nombre:
                  items_unformatted = line.split('>')[1].split(',')
                  items = [] # Lista de strings con nombres de items
                  for item_name in range(len(items_unformatted)-1):
                     items.append(items_unformatted[item_name])
                  precio = float(line.split('|')[1])

                  combo.items = items
                  combo.precio_base = precio

   def agregar_combo(self, nombre, precio, items):
      n = nombre
      p = precio
      i = items

      self.combos.append(Combo(
         n,
         p,
         i
      ))