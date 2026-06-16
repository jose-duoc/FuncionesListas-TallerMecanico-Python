Navegación del Menú
Al iniciar el programa, ingresa el nombre del cliente y el costo de la mano de obra. Luego, interactúa usando las siguientes opciones:
1 para agregar un nuevo artículo/repuesto.
2 para previsualizar el desglose de los gastos actuales.
3 para evaluar y aplicar el recargo de urgencia.
4 para imprimir la boleta definitiva y finalizar la sesión del programa.
"""

```markdown
# 🛠️ Sistema de Cotización para Taller Mecánico

Este proyecto es una aplicación de consola desarrollada en **Python** diseñada para gestionar y calcular las cotizaciones de un taller mecánico. Permite registrar clientes, costos de mano de obra, añadir repuestos, aplicar recargos por urgencia y generar una boleta final detallada con el cálculo automático del IVA (19%).

El sistema está estructurado bajo un diseño modular separado en tres componentes principales: lógica de negocio, interfaz de usuario y el orquestador principal.

---

## 📌 Características Principales

- **Gestión de Clientes:** Registro del nombre del cliente y costo base de la mano de obra.
- **Control de Repuestos:** Adición dinámica de repuestos con sus respectivos precios a la orden de trabajo.
- **Cálculo de Impuestos:** Aplicación automatizada del **IVA (19%)** sobre el valor neto acumulado.
- **Recargo por Urgencia:** Incorporación opcional de un recargo fijo ($60.000) si la orden supera una cantidad crítica de repuestos.
- **Previsualización y Cierre:** Permite ver el estado actual de la boleta en tiempo real o cerrar definitivamente la orden emitiendo el comprobante de pago final.
- **Validación de Datos:** Control de excepciones (`try-except`) para evitar caídas del programa ante ingresos de datos inválidos.

---

## 📂 Estructura del Proyecto

El código se distribuye en tres archivos independientes para asegurar la modularidad y la mantenibilidad del software:

1. **`calculos.py`**: Contiene la lógica matemática y de negocio (funciones con/sin retorno y parámetros).
2. **`interfaz.py`**: Encargado de la interacción visual en la consola, impresiones de menús y formato de boletas.
3. **`main.py`** *(orquestador)*: Contiene el ciclo principal (`while`) y las validaciones de control de flujo del programa.

---

## 💻 Demostración de Funciones Implementadas

El sistema sirve como un excelente ejemplo práctico para entender los diferentes tipos de funciones en Python:

* **Función con parámetros y sin retorno:** `agregar_respuesto(lista_repuestos, nombre, precio)`
* **Función sin parámetros y con retorno:** `obtener_iva()` -> Devuelve `0.19`.
* **Función con parámetros y con retorno:** `calcular_total(lista_repuestos, valor_mano_obra)`
* **Función sin parámetros y sin retorno:** `aplicar_recargo_urgencia(lista_repuestos)`

---

## 🚀 Instrucciones de Uso

### Requisitos Previos
- Tener instalado **Python 3.x**.

### Ejecución
1. Descarga o clona este repositorio en tu máquina local.
2. Asegúrate de guardar los tres bloques de código en archivos llamados `calculos.py`, `interfaz.py` y `main.py` dentro de la misma carpeta.
3. Abre una terminal en dicho directorio y ejecuta:
   ```bash
   python main.py
