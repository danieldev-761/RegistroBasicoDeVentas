clientes= []
productos= []
subordenes= []
ordenes= []

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
            opcion= int(input("Ingrese una opción del menú de opciones (1, 2, 3, 4, 5): "))

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
                        id_actual+=1

                        print("Producto registrado exitosamente.")
                        

                    case 2:
                        
                        print("Cargando Módulo de Registro de Venta...")
                        

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
                        id_actual+=1

                        print("Cliente registrado exitosamente.")

                        productos_existentes= productos.copy()

                        cargar_productos()

                        numero_productos= int(input(f"Bienvenido, {nombre_cliente}. ¿Cuántos productos desea comprar? "))
                        
                        if 0<numero_productos<=len(productos_existentes):


                            for i in range(numero_productos):

                                producto_deseado= int(input(f"Muy bien, {nombre_cliente}. ¿Qué producto(s) desea de la lista? Por favor ingrese el ID de dicho producto: "))

                                
                                cantidad_producto= int(input("Por favor ingrese la cantidad de dicho producto: "))

                                producto_encontrado= buscar_producto(producto_deseado)

                                if producto_encontrado:
                                    print(f"Producto encontrado: {producto_encontrado['nombre']}")

                                    suborden={
                                    "id": id_actual,
                                    "nombre_cliente": nombre_cliente,
                                    "producto": producto_encontrado['nombre'],
                                    "cantidad": cantidad_producto,
                                    "subtotal": producto_encontrado['precio'] * cantidad_producto
                                    
                                    }
                                
                                else:
                                    print("Producto no encontrado.")
                                
                                subordenes.append(suborden)
                                id_actual+=1

                            print(''' ID |  NOMBRE CLIENTE  |   PRODUCTO   |  CANTIDAD   ''')

                            for i in range(len(subordenes)):
                                suborden = subordenes[i]

                            
                                print(f"  {suborden['id']}  | {suborden['nombre_cliente']} |    {suborden['producto']} |    {suborden['cantidad']} |    {suborden['subtotal']}")
                            print("--------------------------------------------------")

                            
                            orden={
                            "id": id_actual,
                            "nombre_cliente": nombre_cliente,
                            "subordenes": subordenes,
                            "total": sum(suborden['subtotal'] for suborden in subordenes)
                            }
                        
                            ordenes.append(orden)
                            id_actual+=1

                            print("Orden registrada exitosamente. Generando resumen de compra...")

                            

                        generar_resumen_de_venta(subordenes)



                    case 3:
                        cargar_clientes()

                    case 4:
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


def buscar_producto(id_producto):
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return None

def generar_resumen_de_venta(subordenes):
    print("--------------- RESUMEN DE COMPRA ---------------\n")
    print("NO.  | NOMBRE CLIENTE | PRODUCTO | CANTIDAD | PRECIO TOTAL")
    print("--------------------------------------------------")

    for suborden in subordenes:
        print(f"  {suborden['id']}  | {suborden['nombre_cliente']} |    {suborden['producto']} |    {suborden['cantidad']} |    {suborden['subtotal']}")
        print(f'''                                                                                                         COSTO TOTAL | {sum(suborden['subtotal'] for suborden in subordenes)}''')
    
    print("--------------------------------------------------")