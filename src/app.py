clientes= []
productos= []

def registroVentas():
    

    id_actual= 1


    while True:
        print('''
        ---------------- SISTEMA DE REGISTRO DE VENTAS ---------------- \n
              ********** MENÚ DE OPCIONES **********
              1. REGISTRAR NUEVO PRODUCTO
              2. REGISTRAR VENTA
              3. VER CLIENTES
              4. VER LISTA DE PRODUCTOS
              5. SALIR


        ''')
        try:
            opcion= int(input("Ingrese una opci´on del menú de opciones (1, 2, 3, 4, 5): "))

            if 0<opcion<=5:

                

                


                match opcion:
                    case 1:
                        print("Cargando Módulo de Productos")
                        print('''
                        ---------------- MÓDULO DE PRODUCTOS ---------------- \n''')

                        nombre_producto= str(input("Ingrese nombre del producto: "))
                        precio= float(input("Ingrese precio del producto: "))
                        cantidad= int(input("Ingrese cantidad del producto: "))

                        producto={
                        "id": id_actual,
                        "nombre": nombre_producto,
                        "precio": precio,
                        "cantidad": cantidad
                        }

                        productos.append(producto)

                        print("Producto registrado exitosamente.")
                        

                    case 2:
                        
                        print("Cargando Módulo de Registro de Venta")
                        

                        nombre_cliente= str(input("Ingrese nombre del cliente: "))
                        membresia_vip= bool(input("¿El cliente es VIP? (True/False): "))
                        documento_identidad= int(input("Ingrese documento de identidad del cliente: "))

                        cliente={
                        "id": id_actual,
                        "nombre": nombre_cliente,
                        "documento_identidad": documento_identidad,
                        "membresia_vip": membresia_vip,
                        "fecha_ultima_compra": None
                        }
                        
                        clientes.append(cliente)

                        print("Cliente registrado exitosamente.")

                        productos_existentes= productos.copy()

                        cargar_productos()
                    

                    case 3:
                        cargar_clientes()

                    case 4:
                        print("Cargando Lista de Productos")
                        cargar_productos()
                        

                    case 5:
                        print("Gracias por utilizar nuestro programa.Saliendo del sistema...")
                        break
            else:
                print("Error: Opción inválida. Ingrese una opción válida (1, 2, 3, 4 o 5).")

        except ValueError:
            print("Error: Campos con valores erróneos")


            

def cargar_productos():
    print("Cargando lista de productos existentes...")
    print("\nREGISTROS GUARDADOS:\n")
    print("ID  | NOMBRE | PRECIO | CANTIDAD")
    print("--------------------------------------------------")

    for prod in productos:
        print(f"  {prod['id']}  | {prod['nombre']} |    {prod['precio']} |    {prod['cantidad']}")
    print("--------------------------------------------------")

def cargar_clientes():
    print("Cargando Lista de Clientes")

    print("Cargando lista de clientes existentes...")
    print("\nREGISTROS GUARDADOS:\n")
    print("ID  | NOMBRE | DOCUMENTO IDENTIDAD | MEMBRESIA VIP")
    print("--------------------------------------------------")

    for client in clientes:
        print(f"  {client['id']}  | {client['nombre']} |    {client['documento_identidad']} |    {client['membresia_vip']}")
    print("--------------------------------------------------")