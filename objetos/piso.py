class Piso:
    # Pasillos, Habitaciones (por cada pasillo)
    def __init__(self, nivel, num_pasillos, num_habitaciones, capacidad_habitacion , costo_habitacion, crucero_padre):
        self.nivel = nivel # String
        self.num_pasillos = num_pasillos # Integer
        self.num_habitaciones = num_habitaciones # Integer
        self.capacidad_habitacion = capacidad_habitacion # Integer'
        self.costo_habitacion = costo_habitacion # Integer
        self.crucero_padre = crucero_padre # Str (nombre de crucero padre)
        self.habitaciones = [] # Lista con objectos habitaciones

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def get_representacion(self):
        pasillos = []
        for habitacion in self.habitaciones:
            if habitacion.identificador[0] not in pasillos: # creando array de todos los pasillos en el piso actual
                pasillos.append(habitacion.identificador[0])
        
        for pasillo in pasillos:
            arr = []
            for habitacion in self.habitaciones:
                if habitacion.identificador[0] == pasillo:
                    if habitacion.ocupado == False:
                        arr.append(habitacion.identificador)
                    elif habitacion.ocupado:
                        arr.append('  ')
            formated_arr = ' '.join(map(str, arr))
            print(f'    Pasillo {pasillo} ➜  {formated_arr}')

    def get_representacion_ocupado(self):
        pasillos = []
        for habitacion in self.habitaciones:
            if habitacion.identificador[0] not in pasillos: # creando array de todos los pasillos en el piso actual
                pasillos.append(habitacion.identificador[0])
        
        for pasillo in pasillos:
            arr = []
            for habitacion in self.habitaciones:
                if habitacion.identificador[0] == pasillo:
                    if habitacion.ocupado:
                        arr.append(habitacion.identificador)
                    elif habitacion.ocupado == False:
                        arr.append('  ')
            formated_arr = ' '.join(map(str, arr))
            print(f'    Pasillo {pasillo} ➜  {formated_arr}')
    
    def get_nivel(self):
        if self.nivel == 'simple':
            return 'Sencillas'
        elif self.nivel == 'premium':
            return 'Premium'
        elif self.nivel == 'vip':
            return 'VIP'
        
    def get_habitaciones_disponibles(self):
        arr = []
        for habitacion in self.habitaciones:
            if habitacion.ocupado == False:
                arr.append(habitacion.identificador)
        return arr