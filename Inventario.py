# 1. Lo que 'vimos' en bodega
cajas_escaneadas = ["BOX-002", "BOX-003", "BOX-999"]

# 
inventario_maestro = [
    {"id": "BOX-001", "nombre": "Silla A", "estado": "Pendiente"},
    {"id": "BOX-002", "nombre": "Silla A", "estado": "Pendiente"},
    {"id": "BOX-003", "nombre": "Escritorio L", "estado": "Pendiente"},
]

# 3. El cruce de datos
for caja in inventario_maestro:
    # ¿Cómo preguntarías aquí si el 'id' de la caja actual 
    # está en la lista de 'cajas_escaneadas'?
    if caja['id'] in cajas_escaneadas:
        print(f'la caja {caja["id"]} ha sido escaneada')
        caja['estado'] = 'RECIBIDA'
    
    # Pista: En Python usamos la palabra 'in' para ver si algo está en una lista.
    pass
print('='*45)
print('-----INVENTARIO ACTUALIZADO-----')
print(inventario_maestro)
print('='*45)