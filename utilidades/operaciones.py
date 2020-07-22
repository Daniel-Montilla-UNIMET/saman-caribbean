# Super lento!
def es_primo(n):
   if n > 1:
      for i in range(2, n):
         if (n % i) == 0:
               return False
      else:
         return True
   else:
      return False

# Aun mas lento
def es_abundante(n):
   divisores = []
   for i in range(n):
      try:
         if n % i == 0:
            divisores.append(i)
      except:
         pass
   
   suma = 0
   for num in divisores:
      suma += num

   if suma > n:
      return True
   else:
      return False