def registroVentas():
    clientes= []
    productos= []

    id_actual= 1


    while True:
        print('''
        ---------------- SISTEMA DE REGISTRO DE VENTAS ---------------- \n
              ********** MENÚ DE OPCIONES **********
              1. REGISTRAR VENTA
              2. REGISTRAR NUEVO PRODUCTO
              3. VER CLIENTES
              4. VER LISTA DE PRODUCTOS
              5. SALIR


        ''')
        try:
            opcion= int(input("Ingrese una opci´on del menú de opciones (1, 2, 3, 4, 5): "))

            if 0<opcion<=4:
                match opcion:
                    case 1:
                        print("Cargando Módulo de Registro de Venta")

                    case 2:
                        print("Cargando Módulo de Productos")

                    case 3:
                        print("Cargando Lista de Clientes")
                        
                    case 4:
                        print("Cargando Lista de Productos")

                    case 5:
                        print("Gracias por utilizar nuestro programa.Saliendo del sistema...")
                        break
            else:
                print("Error: Opción inválida. Ingrese una opción válida (1, 2, 3, 4 o 5).")

        except ValueError:
            print("Error: Campos con valores erróneos")

