import random

# INICIO FUNCIONES

def validarNombreHelado (lista):
    helado = input("Ingrese nombre del helado, solo debe contener letras, FIN para finalizar: ")
    helado=helado.upper()
    while helado.isalpha() == False or helado in lista:
        helado = input("Error ingrese nombre del helado, solo debe contener letras, FIN para finalizar: ")
        helado=helado.upper()
    return helado

def validarNumero(mensaje1, mensaje2):
    error = False
    numeroValido = None
    while True:
        try:
            numeroValido = int(input(mensaje1))
            while numeroValido <= 0:
                numeroValido = int(input(mensaje2))
        except ValueError:
            print("Error")
            error = True
        
        if (numeroValido != None and numeroValido > 0) or error == False:
            break
    return numeroValido

def llenarMatriz(filas, columnas, m):    
    for i in range(filas):
        m.append([])
        for j in range(columnas):
            m[i].append(0)

def pasarMatriz(m):
    try:                                                                    
        archivoParaLeer = open("helados.csv", "rt")                  
    except IOError:
        print("No se pudo encontrar archivo")                               
    else:
        contador = 0
        registro = archivoParaLeer.readline()
        while registro:
            
            id,helado,descripcion,stockInicial = registro.split(";")
            m[contador][0] = int(id)
            m[contador][1] = helado
            m[contador][2] = descripcion
            m[contador][3] = int(stockInicial.rstrip("\n"))
            contador += 1

            registro = archivoParaLeer.readline()


    finally:
        archivoParaLeer.close()

def mostrarListaHelados(listaHelados):
    print("LISTA DE HELADOS")
    print("Codigo", "Nombre")
    for i in range(len(listaHelados)):
        print(i,listaHelados[i])

# FIN FUNCIONES


# PROGRAMA PRINCIPAL

listaHelados = []
id = 0
try:
    archHelados = open("helados.csv", "wt")
except IOError:
    print("No se pudo crear el archivo de Helados")
else:
    helado = validarNombreHelado(listaHelados)
    contadorHelado=1
    while helado !="FIN":
        listaHelados.append(helado)
        descripcion = input("Ingrese una descripcion del helado: ")
        stockInicial = validarNumero("Ingresar numero de stock mayor a cero: ", "Error. Ingresar numero de stock mayor a cero: ") 
        archHelados.write(str(id) + ";" + helado + ";" + descripcion + ";" + str(stockInicial) + "\n")
        helado = validarNombreHelado(listaHelados)
        id +=1
    archHelados.close()


print(listaHelados)

m = []
lineas = len(listaHelados)

llenarMatriz(lineas, 4, m)
pasarMatriz(m)
listaVentas = [0] * lineas

mostrarListaHelados(listaHelados)

precioHelado = 700                                     ###Precio para la porcion de helado (valor arbitrario)
recaudacionTotal = 0                                   ###Inicializacion de la recaudacion en 0
contadorVentas = 0                                     ###Contador cantidad de ventas totales
vaso = 250                                             ###Cantidad de gramos de helado por porcion
stockLimite = 10


### INICIO CARGA VENTAS

ingresoHelado = input("Ingrese codigo de helado. FIN para finalizar.  ") ###VALIDAR: codigo de helado tiene que ser < al len de la lista y mayor a 0

while ingresoHelado != "FIN":
    ##Recorrer aqui la matriz para saber si hay suficiente en stock
    stock = m[int(ingresoHelado)][3]
    cantidadVenta = validarNumero("Ingresar cantidad vendida ", "Error. Cantidad de venta debe ser mayor a cero, reingresar: ") ### numero entero mayor a 0
    while (cantidadVenta * vaso) > stock:
        cantidadVenta = int(input("Cantidad vendida es mayor al stock disponible, reingrese cantidad vendida: ")) ### numero entero mayor a 0

    
    listaVentas[int(ingresoHelado)] += cantidadVenta
    m[int(ingresoHelado)][3] -= cantidadVenta*vaso
    contadorVentas += cantidadVenta
    recaudacionTotal += (precioHelado * cantidadVenta)                      ### acumulacion de la recaudacion total

    ingresoHelado = input("Ingrese codigo de helado. FIN para finalizar.  ") ###VALIDAR: codigo de helado tiene que ser < al len de la lista y mayor a 0

# FIN CARGA VENTAS

# MUESTRA EN PANTALLA DE RESULTADOS AL FINAL DEL DIA
print("La cantidad de ventas al final del día fue ", contadorVentas)
print("La recaudación total al final del día fue ", recaudacionTotal, "$")

# Muestra de helados con mayor y menor venta
menorVenta = listaVentas.index(min(listaVentas))                     ### indice de menor venta
mayorVenta = listaVentas.index(max(listaVentas))                     ### indice de mayor venta

print("El helado con mayor venta fue", listaHelados[mayorVenta])
print("El helado con menor venta fue", listaHelados[menorVenta])


stockTotal = 0                                                      ### calculamos la suma del stock total de los helados
for i in range(lineas):
    stockTotal+=m[i][3]
    if m[i][3]<stockLimite:
        print("Helado sabor", m[i][2], "necesita reposicion de stock\n")


print(m)

try:
    archFinal = open("Final.csv", "wt")
except IOError:
    print("No se pudo crear el archivo final")
else:
    for i in range(lineas):
        archFinal.write(str(m[i][1]) + ";" + str(m[i][3])+ ";" + str(stockLimite) + ";" + str(int((m[i][3]/stockTotal)*100))+"%" + "\n")
    archFinal.close()