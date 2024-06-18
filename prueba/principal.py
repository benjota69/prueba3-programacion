import funciones as fn

clientes = []

while True:
    print("Menú de Pedidos -(Gaxplosive)-")
    print("[1] - Registrar Pedido")
    print("[2] - Listar todos los Pedidos")
    print("[3] - Imprimir Hoja de Ruta")
    print("[4] - Salir del Programa")
    print("")
    opc = int(input("Ingrese la opción: "))

    if opc == 1:
        fn.registrar_pedido(clientes)
    elif opc == 2:
        fn.listar_pedido(clientes)
    elif opc == 3:
        fn.imprimir_hojaruta(clientes)
    elif opc == 4:
        print("Has salido con exito del sistema ADIOS!!")
        break
    