#Función con parámetros y sin retorno
def agregar_respuesto(lista_repuestos,nombre, precio):
    lista_repuestos.append({"nombre":nombre,"precio":precio})
    print(f"{nombre} agregado a la orden.")
#Función sin parámetros y con retorno
def obtener_iva():
    return 0.19
#Función con parámetros y con retorno
def calcular_total(lista_repuestos,valor_mano_obra):
    neto = valor_mano_obra
    for repuesto in lista_repuestos:
        neto += repuesto["precio"]
    iva = neto * obtener_iva()
    return neto + iva
#Función sin parámetros y sin retorno
def aplicar_recargo_urgencia(lista_repuestos):
    if len(lista_repuestos) > 3:
        lista_repuestos.append({"nombre":"RECARGO URGENCIA","precio":60000})