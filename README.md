# 🧮 Calculadora de Sueldo Neto

Este es un programa en Python con Reflex (Python Web Framework) que permite calcular el sueldo neto de un empleado en República Dominicana, aplicando descuentos reales de seguridad social, ISR y bonificación.

## Versión de Python

- Python 3.12.10

## Requisitos

- Librería externa: reflex

## ¿Qué hace este programa?

- Ingresar el sueldo bruto.
- Especificar si la empresa ofrece bonificación.
- Ingresar otros descuentos (ej. préstamos, cooperativa).
- Ver el cálculo automático de:
  - Descuento por Seguridad Social (5.91%)
  - ISR (15% si gana más de RD$34,685)
  - Bonificación (10% si aplica)
  - Sueldo Neto final

La aplicación se ejecuta como una página web local y actualiza los datos en tiempo real.

---

## Instalación y Ejecución (paso a paso usando Git Bash)

### 1. Clona el repositorio desde GitHub:


git clone https://github.com/YandellCM/calculadora_sueldo_neto.git
cd calculadora_sueldo_neto

### 2. Crea el entorno virtual:

python -m venv venv

### 3. Activa el entorno virtual:

source venv/Scripts/activate

### 4. Instala las dependencias necesarias:

pip install -r requirements.txt

### 5. Ejecuta el programa Reflex:

reflex run

### 6. Abre tu navegador en esta dirección:

http://localhost:3000
