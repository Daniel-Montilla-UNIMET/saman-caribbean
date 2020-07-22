class Menu: # Para simplificar los menus!
   def __init__(self, options):
      self.options = options # Arr
   
   def get_menu(self):
      print('  E̲s̲c̲o̲ja̲ o̲pc̲i̲ó̲n̲:')
      for option in range(len(self.options)):
         print(   f'[{option + 1}] {self.options[option]}')

      return input('\n')
