import statistics

print("Desarrollado por Cristhian Mendoza Ponce ")
datos = []

print("Elija una opción ")
print("1 media ")
print("2 mediana ")
print("3 moda ")

opc=int(input("Ingrese la opcion requerida : "))


while opc == 1:

    print("Esta calculando la Media ")
    veces=int(input("Ingrese la cantidad de datos a ingresar : "))
    x=0
    while x < veces:
        valor=float(input("Ingrese un valor :"))
        x=x+1
        datos.append(valor)

    print("La media es ")

    print(statistics.mean(datos))
    opc=0

while opc == 2:

    print("Esta calculando la Mediana ")
    veces=int(input("Ingrese la cantidad de datos a ingresar : "))
    x=0
    while x < veces:
        valor=float(input("Ingrese un valor :"))
        x=x+1
        datos.append(valor)

    print("La mediana es ")

    print(statistics.median(datos))
    opc=0

while opc == 3:

    print("Esta calculando la Moda ")
    veces=int(input("Ingrese la cantidad de datos a ingresar : "))
    x=0
    while x < veces:
        valor=float(input("Ingrese un valor :"))
        x=x+1
        datos.append(valor)

    print("La moda es ")

    print(statistics.mode(datos))
    opc=0





input( "Presione Enter para finalizar...")

