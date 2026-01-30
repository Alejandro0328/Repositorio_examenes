def cargar_saldo(saldo):
    monto = float(input("Ingrese el monto a depositar: "))
    if monto > 0:
        nuevo_saldo = saldo + monto
        print(f"Carga exitosa. Nuevo saldo: ${nuevo_saldo}")
        return nuevo_saldo 
    else:
        print("Error: El monto debe ser mayor a cero.")
        return saldo

def retirar_pago(saldo_actual):
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= 0:
        print("Error: Monto inválido.")
    elif monto > saldo_actual:
        print("Error: Fondos insuficientes.")
    else:
        saldo_actual -= monto
        print(f"Pago realizado. Saldo restante: ${saldo_actual}")
    return saldo_actual

def main():
    saldo = 1000 
    
    while True:
        print("\n--- BIENVENIDO A TU CAJERO AUTOMATICO---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("0. Salir") # Cambiado a 0 según el requisito
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Saldo actual: ${saldo}") # Quitamos el 'saldo ='
        elif opcion == "2":
            saldo = cargar_saldo(saldo)
        elif opcion == "3":
            saldo = retirar_pago(saldo)
        elif opcion == "0": # Condición de salida única y limpia
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

main()