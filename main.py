"""Catálogo de La Rebajita. Datos en memoria: [nombre, categoría, precio]."""

# No usar [[], []]: serían dos registros sin nombre, categoría ni precio.
productos = []

while True:
    print("=" * 40)
    print('Supermercado y Distribuidora de Alimentos "La Rebajita"')
    print("Sistema de gestión de productos")
    print("=" * 40)
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegí una opción (1-5): ").strip()

    if opcion == "1":
        print("--- Agregar producto ---")

        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            print("Error: el nombre que coloque no debe de estar vacío.")
            nombre = input("Nombre del producto: ").strip()

        categoria = input("Categoría del producto: ").strip()
        while categoria == "":
            print("Error: la categoría que coloque no debe estar vacía.")
            categoria = input("Categoría del producto: ").strip()

        # El orden de las condiciones evita convertir texto inválido con int().
        # Límite de 12 dígitos para rechazar entradas numéricas desmesuradas.
        precio_str = input("Precio (sin centavos): ").strip()
        while (
            not precio_str.isascii()
            or not precio_str.isdigit()
            or len(precio_str) > 12
            or int(precio_str) <= 0
        ):
            print("Error: ingresá un entero positivo de hasta 12 dígitos.")
            precio_str = input("Precio (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre, categoria, precio]
        productos.append(datos)
        print(f"Se agregó el producto: {nombre}.")

    elif opcion == "2":
        print("--- Lista de productos ---")
        if len(productos) == 0:
            print("Todavía no hay productos incluidos.")
        else:
            # i empieza en 0; el número visible i + 1 empieza en 1.
            for i in range(len(productos)):
                print(
                    f"ID: {i + 1}\n"
                    f"-Nombre: {productos[i][0]}\n"
                    f"-Categoría: {productos[i][1]}\n"
                    f"-Precio: ARS $ {productos[i][2]}\n"
                )

    elif opcion == "3":
        print("--- Buscar producto ---")
        if len(productos) == 0:
            print("Todavía no hay productos incluidos.")
        else:
            busqueda = input("Nombre del producto a buscar: ").strip().lower()
            while busqueda == "":
                print("Error: escribe algo para buscar.")
                busqueda = input("Nombre del producto a buscar: ").strip().lower()

            encontrado = 0
            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(
                        f"ID: {i + 1}\n"
                        f"-Nombre: {productos[i][0]}\n"
                        f"-Categoría: {productos[i][1]}\n"
                        f"-Precio: ARS {productos[i][2]}\n"
                    )
                    encontrado += 1

            if encontrado == 0:
                print("No se encontró ningún resultado.")
            else:
                print(f"Productos encontrados: {encontrado}.")

    elif opcion == "4":
        print("--- Eliminar producto ---")
        if len(productos) == 0:
            print("Todavía no hay productos incluidos.")
        else:
            for i in range(len(productos)):
                print(
                    f"{i + 1}. {productos[i][0]} - "
                    f"{productos[i][1]} - ARS $ {productos[i][2]}"
                )

            # Primero comprobamos el texto y después el rango del número.
            id_eliminar = input("Número de producto a eliminar: ").strip()
            while (
                not id_eliminar.isascii()
                or not id_eliminar.isdigit()
                or len(id_eliminar) > 12
                or int(id_eliminar) < 1
                or int(id_eliminar) > len(productos)
            ):
                print(f"Error: elegí un número entre 1 y {len(productos)}.")
                id_eliminar = input("Número de producto a eliminar: ").strip()
            posicion = int(id_eliminar) - 1
            eliminado = productos.pop(posicion)
            print(f"Se eliminó el producto: {eliminado[0]}.")

    elif opcion == "5":
        print("¡Gracias por usar el sistema de La Rebajita!")
        break

    else:
        print("Opción no válida. Tienes que elegir entre 1 y 5.")

