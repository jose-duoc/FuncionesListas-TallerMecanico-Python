def mostrar_encabezado():
    print("\n===============================")
    print("         TALLER MECÁNICO         ")
    print("\n===============================")
def limpiar_pantalla():
    print("\n"*15)
def menu_opciones():
    print("1.- Agregar repuesto: ")
    print("2.- Ver boleta actual (Previsualizar): ")
    print("3.- Aplicar Urgencia: ")
    print("4.- Generar boleta final y cerrar orden:  ")
def notificar_registro_exitoso(nombre):
    print(f"{nombre} agregado a la orden")
def notificar_recargo_evaluado():
    print("[NOTIFICACIÓN] Se ha incorporado un recargo por urgencia")
def mostrar_boleta_final(cliente,lista_repuestos,mano_obra,total_pagar):
    print("\n ----- BOLETA CLIENTE -------")
    print(f"Cliente: {cliente}")
    print("-------------------------------")
    print(f"Mano de obra: ${mano_obra}")
    print("Repuestos utilizados")
    for r in lista_repuestos:
        print(f"- {r['nombre']}: ${r['precio']}")
    print("-------------------------------")
    print(f"TOTAL A PAGAR (IVA inc.): ${int(total_pagar)}")
    print("================================")