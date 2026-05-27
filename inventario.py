# ==========================================
# SISTEMA DE AUDITORÍA DE INVENTARIO
# FUNDAMENTOS DE PROGRAMACIÓN - FASE 5
# ==========================================

# Matriz de inventario
inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 15, 10],
    ["A103", "Monitor", 3, 8],
    ["A104", "USB", 20, 15],
    ["A105", "Impresora", 2, 6]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Título del reporte
print("======================================")
print(" REPORTE DE REABASTECIMIENTO ")
print("======================================")

# Recorrer la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamado de la función
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultados
    print("--------------------------------------")
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock Actual:", stock_actual)
    print("Stock Mínimo:", stock_minimo)
    print("Cantidad a Pedir:", cantidad_pedir)

print("--------------------------------------")
print("Fin del reporte")
