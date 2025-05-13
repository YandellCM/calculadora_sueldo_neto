import reflex as rx  # Librería principal de Reflex

# Porcentajes oficiales para los cálculos
tss = 0.0591  # Seguridad Social
isr = 0.15    # Impuesto Sobre la Renta (si sueldo > 34685)
bono = 0.10   # Bonificación (si aplica)

# Clase que guarda los datos del formulario y realiza los cálculos
class Estado(rx.State):
    sueldo = 0.0
    otros = 0.0
    con_bono = False

    descuento_seg = 0.0
    descuento_isr = 0.0
    bonificacion = 0.0
    sueldo_neto = 0.0

    def calcular(self):
        self.descuento_seg = self.sueldo * tss
        self.descuento_isr = self.sueldo * isr if self.sueldo > 34685 else 0
        self.bonificacion = self.sueldo * bono if self.con_bono else 0
        self.sueldo_neto = (
            self.sueldo - self.descuento_seg - self.descuento_isr - self.otros + self.bonificacion
        )

# Interfaz principal de la página web
def vista():
    return rx.center(
        rx.vstack(
            rx.heading("Calculadora de Sueldo Neto", size="5"),  # ✅ Tamaño corregido
            rx.input(placeholder="Escribe tu sueldo bruto", on_change=Estado.set_sueldo),
            rx.input(placeholder="Escribe otros descuentos", on_change=Estado.set_otros),
            rx.checkbox("¿La empresa da bonificación?", on_change=Estado.set_con_bono),
            rx.button("Calcular", on_click=Estado.calcular),
            rx.divider(),
            rx.text("Descuento Seguridad Social: ", rx.var(Estado.descuento_seg)),
            rx.text("Descuento ISR: ", rx.var(Estado.descuento_isr)),
            rx.text("Bonificación: ", rx.var(Estado.bonificacion)),
            rx.text("Sueldo Neto: ", rx.var(Estado.sueldo_neto)),
            spacing="2em"
        ),
        padding="2em"
    )

# Registro de la aplicación
app = rx.App()
app.add_page(vista)
