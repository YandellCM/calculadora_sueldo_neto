import reflex as rx

# Porcentajes oficiales para los cálculos
tss = 0.0591  # Seguridad Social
isr = 0.15    # Impuesto Sobre la Renta (si sueldo > 34685)
bono = 0.10   # Bonificación (si aplica)

# Clase que guarda los datos del formulario y realiza los cálculos
class Estado(rx.State):
    sueldo: float = 0.0
    otros: float = 0.0
    con_bono: bool = False

    descuento_seg: float = 0.0
    descuento_isr: float = 0.0
    bonificacion: float = 0.0
    sueldo_neto: float = 0.0

    def set_sueldo(self, sueldo_str: str):
        try:
            self.sueldo = float(sueldo_str)
        except ValueError:
            self.sueldo = 0.0
            print("Entrada de sueldo inválida")

    def set_otros(self, otros_str: str):
        try:
            self.otros = float(otros_str)
        except ValueError:
            self.otros = 0.0
            print("Entrada de otros descuentos inválida")

    def set_con_bono(self, con_bono: bool):
        self.con_bono = con_bono

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
            rx.heading("Calculadora de Sueldo Neto", size="5"),
            rx.input(
                placeholder="Escribe tu sueldo bruto",
                on_change=Estado.set_sueldo,
                type="number",  # Sugerir teclado numérico
            ),
            rx.input(
                placeholder="Escribe otros descuentos",
                on_change=Estado.set_otros,
                type="number",  # Sugerir teclado numérico
            ),
            rx.checkbox("¿La empresa da bonificación?", on_change=Estado.set_con_bono),
            rx.button("Calcular", on_click=Estado.calcular),
            rx.divider(),
            rx.text("Descuento Seguridad Social: ", rx.var(Estado.descuento_seg)),
            rx.text("Descuento ISR: ", rx.var(Estado.descuento_isr)),
            rx.text("Bonificación: ", rx.var(Estado.bonificacion)),
            rx.text("Sueldo Neto: ", rx.var(Estado.sueldo_neto)),
            spacing="2em",
        ),
        padding="2em",
    )

# Registro de la aplicación
app = rx.App()
app.add_page(vista)