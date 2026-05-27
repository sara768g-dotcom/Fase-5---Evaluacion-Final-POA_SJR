#Nombre del estudiante: Sara J. Ruiz
#Grupo:213022_560
#Programa: Ingeniería en Sistemas
#Código fuente: Autoría propia
#Problema 3 - Auditoria de Inventarios

#Funcion para calcular el stock a pedir
def calcular_stock_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

inventario = []
continuar = True

print("SISTEMA DE AUDITORIA DE INVENTARIOS")

while continuar:
    print("\n1. Agregar producto")
    print("2. Verificar inventario")
    print("3. Ver pedidos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            cantidad = int(input("Ingrese la cantidad de artículos a registrar: "))
        except ValueError:
            print("Debe ingresar un número entero.")
            continue

        for i in range(cantidad):
            print("\nArtículo", i + 1)
            codigo = input("Ingrese el código del artículo: ")
            nombre = input("Ingrese el nombre del artículo: ")
            try:
                stock_actual = int(input("Stock actual: "))
                stock_minimo = int(input("Stock mínimo: "))
            except ValueError:
                print("El stock debe ser un número entero.")
                continue

            articulo = [codigo, nombre, stock_actual, stock_minimo]
            inventario.append(articulo)
            print("Artículo registrado exitosamente.")

    elif opcion == "2":
        if len(inventario) == 0:
            print("No hay artículos registrados.")
        else:
            print("\nInventario")
            for articulo in inventario:
                print("--------------------------------")
                print("Código:", articulo[0])
                print("Nombre:", articulo[1])
                print("Stock Actual:", articulo[2])
                print("Stock Mínimo:", articulo[3])

    elif opcion == "3":
        if len(inventario) == 0:
            print("No hay artículos registrados.")
        else:
            print("\nPedidos")
            hay_pedidos = False
            for articulo in inventario:
                codigo = articulo[0]
                nombre = articulo[1]
                stock_actual = articulo[2]
                stock_minimo = articulo[3]
                cantidad_pedir = calcular_stock_a_pedir(stock_actual, stock_minimo)
                if cantidad_pedir > 0:
                    print("--------------------------------")
                    print("Código:", codigo)
                    print("Nombre:", nombre)
                    print("Cantidad a pedir:", cantidad_pedir)
                    hay_pedidos = True
            if not hay_pedidos:
                print("No hay pedidos pendientes.")

    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        continuar = False

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
