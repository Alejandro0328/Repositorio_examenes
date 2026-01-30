def sistema_nequi_pro():
    saldo = 0
    historial = []  # Lista para guardar los textos de cada movimiento

    while True:
        print("\n" + "="*20)
        print(" NEQUI PRO - MENÚ")
        print("="*20)
        print("1. Cargar saldo\n2. Pagar\n3. Transferir\n4. Ver Movimientos\n5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            print("Cerrando sesión... ¡Adiós!")
            break

        # Usamos try-except para capturar errores de escritura (letras en vez de números)
        try:
            if opcion == "1":
                monto = float(input("¿Cuánto desea cargar?: "))
                if monto > 0:
                    saldo += monto
                    historial.append(f"Carga: +${monto}") # Guardamos en la lista
                    print(f"Éxito. Saldo actual: ${saldo}")
                else:
                    print("Error: El monto debe ser positivo.")

            elif opcion == "2":
                monto = float(input("¿Cuánto va a pagar?: "))
                if 0 < monto <= saldo:
                    saldo -= monto
                    historial.append(f"Pago: -${monto}")
                    print(f"Pago realizado. Saldo restante: ${saldo}")
                else:
                    print("Monto inválido o fondos insuficientes.")

            elif opcion == "3":
                cel = input("Número de celular (10 dígitos): ")
                if len(cel) == 10:
                    monto = float(input("Monto a enviar: "))
                    if 0 < monto <= saldo:
                        saldo -= monto
                        historial.append(f"Transf. a {cel}: -${monto}")
                        print("Transferencia exitosa.")
                    else:
                        print("Monto inválido o saldo insuficiente.")
                else:
                    print("Error: El celular debe tener 10 dígitos.")

            elif opcion == "4":
                print("\n--- HISTORIAL DE MOVIMIENTOS ---")
                if len(historial) == 0:
                    print("No hay movimientos registrados.")
                else:
                    # Usamos 'for' e 'in range' para enumerar los movimientos
                    for i in range(len(historial)):
                        # i empieza en 0, por eso sumamos 1 para que el usuario vea "1. Carga..."
                        print(f"{i + 1}. {historial[i]}")
                    print(f"SALDO TOTAL: ${saldo}")

            else:
                print("Opción no válida.")

        except ValueError:
            # Este bloque se activa si el usuario escribe texto donde se esperaba un número
            print("¡ERROR! Por favor, ingrese solo valores numéricos.")

# Ejecutar
sistema_nequi_pro()