import os
os.system("cls")

# productos = modelo : [marca, pantall, ram, disco, GB de DD, procesador, video]

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
             
# stock = {modelo: [PRECIO, STOCK]}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}

def validar_opcion(): 
    while True: 
        try: 
            opcion = int(input("\nIngrese la opción deseada: > "))
            if 0 < opcion < 5: 
                return opcion 
            else: 
                print("\nDebe seleccionar una opción válida!!!")

        except ValueError: 
            print("\nDebe seleccionar una opción válida!!!")

def stock_marca(marca):
    existe_modelo = False
    stock_total = 0
    for modelo, marca_pc in productos.items(): 
        if marca.lower() == marca_pc[0].lower(): 
            stock_total += stock[modelo][1]
            existe_modelo = True
    
            print(f"Hay {stock[modelo][1]} {marca_pc[0]} de este modelo.")
    if existe_modelo == True:
        print(f"Hay un total de {stock_total} computadores {marca}") 
    else: 
        print("No existe ese modelo...")

def busqueda_precio(p_min , p_max): 

    # VERIFICAMOS QUE SEAN NÚMEROS ENTEROS. 
    while True: 
        try: 
            p_min = int(p_min)
            p_max = int(p_max)
            break
         
        except: 
            print("\nDebe ingresar valores enteros!!!.")
            p_min = input("\nIngrese el precio mínimo que desea buscar: > ")
            p_max = input("Ingrese el precio mínimo que desea buscar: > ")
    
    computadores_encontrados = []
    for modelo, (precio, cantidad) in stock.items(): 
        if p_min <= precio <= p_max and cantidad > 0: 
            computadores_encontrados.append(f"{productos[modelo][0]} -- {modelo}")
    print()
    if computadores_encontrados: 
        for computadores in sorted(computadores_encontrados): 
            print(computadores)
    else: 
        print("\nNo hay notebooks en ese rango de precios")

def actualizar_precio(modelo, p): 
    for modelo_diccionario, precio in stock.items():
        if modelo.lower() == modelo_diccionario.lower():
            precio[0] = p
            return True
        else: 
            return False


           


def menu():  
    while True: 
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir")
        opcion = validar_opcion()
        if opcion == 1: 
            marca = input("\nIngrese el nombre de la marca que desea buscar: > ")
            stock_marca(marca)

        elif opcion == 2: 
            precio_minimo = input("\nIngrese el precio mínimo que desea buscar: > ")
            precio_maximo = input("Ingrese el precio máximo que desea buscar: > ")
            busqueda_precio(precio_minimo, precio_maximo)

        elif opcion == 3: 
            modelo = input("\nIngresa el nombre del modelo: > ")
            while True: 
                try:
                    precio_actualizado = int(input("Ingresa el nuevo valor del modelo: > "))
                    if precio_actualizado > 0: 
                        break
                    else: 
                        print("\nEl nuevo precio tiene que ser un número entero")

                except:
                    print("\nEl nuevo precio tiene que ser un número entero")
            verificacion_cambio = actualizar_precio(modelo, precio_actualizado)

            while True: 
                
                if verificacion_cambio == True: 
                    print("\nPrecio actualizado!!!!")
                else: 
                    print("\nEl modelo no existe!!")

                respuesta = input("\n¿Desea actualizar el precio de otro notebook?     --->  |SÍ| - |NO| ")

                if respuesta.upper() == "SÍ" or respuesta.upper() == "SI":
                    print()
                    modelo = input("Ingresa el nombre del modelo: > ")
                    precio_actualizado = input("Ingresa el nuevo valor del modelo: > ")
                    verificacion_cambio = actualizar_precio(modelo, precio_actualizado)

                elif respuesta.upper() == "NO": 
                    break
                else: 
                    print("\nSu respuesta no ha sido identificada.")

                    

        elif opcion == 4: 
            print("\nPROGRAMA FINALIZADO\n.")
            break
        
menu()

