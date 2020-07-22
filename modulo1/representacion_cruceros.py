def representar_cruceros(cruceros):
   for crucero in range(len(cruceros)):  # Imprime toda la info de cada objeto
      print(
   f"""        ✦ Crucero #{crucero + 1}
   Nombre de Crucero ➜  {cruceros[crucero].get_nombre()}
   Ruta ➜  {cruceros[crucero].get_ruta()}
   Fecha de salida ➜  {cruceros[crucero].get_fecha_salida()}
   Costos de boletos ➜  Sencillo: ${cruceros[crucero].get_costo('sencillo')}, Premium: ${cruceros[crucero].get_costo('premium')}, VIP: ${cruceros[crucero].get_costo('vip')}
   Capacidad de habitaciones ➜  Sencillo: {cruceros[crucero].get_capacidad('sencillo')}, Premium: {cruceros[crucero].get_capacidad('premium')}, VIP: {cruceros[crucero].get_capacidad('vip')}
   """)
   