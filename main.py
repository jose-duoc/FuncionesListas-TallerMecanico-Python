import calculos
import interfaz

def orquestador_programa():
    #Declación de variables
    nombre_cliente = input("Nombre del cliente: ").upper()
    mano_obra = 0
    repuestos_lista = []
    try:
        mano_obra = int(input("Costo de la mano de obra ($): "))
    except ValueError :
        print("Error de ingreso ")
    activo = True
    #Iteración e interacción con el cliente
    while activo:
        interfaz.mostrar_encabezado()
        interfaz.menu_opciones()
        try:
            opcion = int(input("\n Selecciona una opción (1-4): "))
        except ValueError:
            print("Por favor, ingrese un número entero")
            continue
        if opcion == 1:
            nombre_r = input("Nombre del repuesto: ")
            try:
                precio_r = int(input("Precio del repuesto ($): "))
                calculos.agregar_respuesto(repuestos_lista,nombre_r,precio_r)
                interfaz.notificar_registro_exitoso(nombre_r)
            except ValueError:
                print("Error: el precio debe ser un número entero")
        elif opcion == 2:
            interfaz.limpiar_pantalla()
            total_actual = calculos.calcular_total(repuestos_lista,mano_obra)
            interfaz.mostrar_boleta_final(nombre_cliente,repuestos_lista,mano_obra,total_actual)
        elif opcion == 3:
            calculos.aplicar_recargo_urgencia(repuestos_lista)
            interfaz.notificar_recargo_evaluado()
        elif opcion == 4: 
            interfaz.limpiar_pantalla()
            total_final= calculos.calcular_total(repuestos_lista,mano_obra)
            interfaz.mostrar_boleta_final(nombre_cliente,repuestos_lista,mano_obra,total_final)
            activo = False
        else:
            print("Opción fuera de rango")
if __name__ == "__main__":
    orquestador_programa()
