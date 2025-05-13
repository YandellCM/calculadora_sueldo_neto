def calcular_sueldo_neto():
    """
    Calcula el sueldo neto en la República Dominicana considerando
    seguridad social, ISR según tramos anuales y bonificación.
    """

    # Porcentajes aplicables
    TSS_EMPLEADO = 0.0287
    SFS_EMPLEADO = 0.0304
    BONO_PORCENTAJE = 0.15

    # Tramos anuales de ISR ajustados (con inflación estimada)
    TRAMOS_ISR = [
        (0.00, 456441.76, 0.00),        # Exento
        (456441.77, 685517.66, 0.15),
        (685517.67, 952417.77, 0.20),
        (952417.78, float('inf'), 0.25)
    ]

    # Entradas
    while True:
        try:
            sueldo_bruto = float(input("Ingrese el Sueldo Bruto mensual: RD$ "))
            if sueldo_bruto >= 0:
                break
            print("Debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida.")

    while True:
        try:
            otros_descuentos = float(input("Ingrese otros descuentos mensuales (0 si no aplica): RD$ "))
            if otros_descuentos >= 0:
                break
            print("Debe ser un número positivo o cero.")
        except ValueError:
            print("Entrada inválida.")

    aplica_bonificacion = input("¿Aplica bonificación? (si/no): ").strip().lower() == "si"

    # Cálculos
    descuento_tss = sueldo_bruto * TSS_EMPLEADO
    descuento_sfs = sueldo_bruto * SFS_EMPLEADO
    total_descuento_seguridad = descuento_tss + descuento_sfs

    retencion_isr = 0.0
    sueldo_anual = sueldo_bruto * 12

    for minimo, maximo, porcentaje in TRAMOS_ISR:
        if minimo <= sueldo_anual <= maximo:
            exceso = sueldo_anual - minimo
            retencion_anual = exceso * porcentaje
            retencion_isr = retencion_anual / 12
            break
        elif sueldo_anual > maximo and maximo != float('inf'):
            exceso = maximo - minimo
            retencion_isr += (exceso * porcentaje) / 12
        elif sueldo_anual > maximo and maximo == float('inf'):
            exceso = sueldo_anual - minimo
            retencion_isr += (exceso * porcentaje) / 12
            break

    bonificacion = sueldo_bruto * BONO_PORCENTAJE if aplica_bonificacion else 0.0

    sueldo_neto = sueldo_bruto - total_descuento_seguridad - retencion_isr - otros_descuentos + bonificacion

    # Resultados
    print("\n--- Resultados del Cálculo de Sueldo Neto ---")
    print(f"Sueldo Bruto: RD$ {sueldo_bruto:.2f}")
    print(f"Descuento TSS (2.87%): RD$ {descuento_tss:.2f}")
    print(f"Descuento SFS (3.04%): RD$ {descuento_sfs:.2f}")
    print(f"Total Seguridad Social: RD$ {total_descuento_seguridad:.2f}")
    print(f"Retención ISR: RD$ {retencion_isr:.2f}")
    print(f"Otros Descuentos: RD$ {otros_descuentos:.2f}")
    print(f"Bonificación: RD$ {bonificacion:.2f}" if aplica_bonificacion else "Bonificación: No aplica")
    print(f"**Sueldo Neto: RD$ {sueldo_neto:.2f}**")

if __name__ == "__main__":
    calcular_sueldo_neto()
