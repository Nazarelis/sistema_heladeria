import random
listaHelados=[]

try:
    archHelados = open("helados.csv", "wt")
except IOError:
    print("No se pudo crear el archivo de Helados")
else:
    helado = input("Ingrese nombre del helado, FIN para finalizar: ")
    
    listaHelados.append(helado)
    while helado !="FIN":
        id = random.randint(1,10)
        descripcion = input("Ingrese una descrición del helado: ")
        stockInicial = int(input("Ingresar numero de stock mayor a cero: ")) 
        archHelados.write(str(id)+";"+helado+";"+descripcion+";"+str(stockInicial)+"\n")
        helado = input("Ingrese nombre del helado, FIN para finalizar: ")
    archHelados.close()
       
    