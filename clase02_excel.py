import pandas as pd

df = pd.read_excel('inventario_bodega.xlsx')

cajas_escaneadas = ['BOX-002', 'BOX-004']


for codigo in cajas_escaneadas:

    df.loc[df['ID_Caja'] == codigo, 'Estado'] = 'Recibida'

df.to_excel('inventario_bodega_actualizado.xlsx', index=False)

print('Inventario actualizado y guardado en "inventario_bodega_actualizado.xlsx"')

df2 = pd.read_excel('inventario_bodega_actualizado.xlsx')


print('Contenido del inventario actualizado:')
print('='*45)
print(df2)
print('='*45)