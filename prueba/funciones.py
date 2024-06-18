SECTORES = ['centro','colina','industrias']

def registrar_pedido(clientes):
    nombre = input("Ingrese Nombre y Apellido del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    sector = input("Ingrese el sector(Centro/Colina/Industrias): ").lower()
    while sector not in SECTORES:
        print("Sector incorrecto, por favor intentelo nuevamente")
        sector = input("Ingrese el sector (Centro/Colina/Industrias): ").lower()
    cantidadCilindros5kg = int(input("Ingrese cuantos cilindros de 5KG querrá: "))
    cantidadCilindros15kg = int(input("Ingrese cuantos cilindros de 15KG querrá: "))
    cantidadCilindros45kg = int(input("Ingrese cuantos cilindros de 45KG querrá: "))
   
    print("Pedido registrado con éxito!")
    print("")

    clientes.append({
        'Cliente' : nombre,
        'Direccion' : direccion,
        'Sector' : sector,
        'Cil. 5kg' : cantidadCilindros5kg,
        'Cil. 15kg' : cantidadCilindros15kg,
        'Cil. 45kg' : cantidadCilindros45kg
    })

def listar_pedido(clientes):
    print("Lista de Clientes: ")
    for cliente in clientes:
        print(cliente)
        print("")

def imprimir_hojaruta(clientes):
    sectorseleccionado = input("Ingrese el sector para imprimir la hojaruta : ").lower()
    if sectorseleccionado in SECTORES:
        clientes_a_imprimir = []
        for cliente in clientes:
            if cliente['Sector'] == sectorseleccionado:
                clientes_a_imprimir.append(cliente)
        nombredelarchivo = f'hojaruta_{sectorseleccionado}.txt'
        print("Hoja de Ruta imprimida con éxito!")
    else:
        print("Sector incorrecto!")
        return

    with open(nombredelarchivo,'w') as archivo:
        for cliente in clientes_a_imprimir:
            archivo.write(f"Cliente : {cliente['Cliente']}\n")
            archivo.write(f"Direccion : {cliente['Direccion']}\n")   
            archivo.write(f"Sector : {cliente['Sector']}\n")   
            archivo.write(f"Cil. 5kg : {cliente['Cil. 5kg']}\n")   
            archivo.write(f"Cil. 15kg : {cliente['Cil. 15kg']}\n")
            archivo.write(f"Cil. 45kg : {cliente['Cil. 45kg']}\n") 
