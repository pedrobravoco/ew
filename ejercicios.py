def dar_vuelta(x):
    lista=[]
    palabra=""
    for i in x:
        palabra=i
        vue=palabra[::-1]
        lista.append(vue)
    print (lista)
def largo_palabra(x):
    palabra=""
    largo=0
    for i in x:        
        if largo<len(i):
            palabra=i
            largo=(len(i))
    print(palabra)   
def menu():
    print("opcion 1: largo de una palabra")
    print("opcion 2: dar vuelta todas las palbras de una lista")
    print("opcion 3: adios")
menu()
opcionmenu=int(input("ingrese su opcion: "))
lista=[]
if opcionmenu==1:
    numero=int(input("cuantas palabras quiere ingresar: "))
    for i in range(numero):
        palabra=input("ingrese una palabra: ")
        lista.append(palabra)    
    largo_palabra(lista)   
elif opcionmenu==2:
    numero=int(input("cuantas palabras quiere ingresar: "))
    for i in range(numero):
        palabra=input("ingrese una palabra: ")
        lista.append(palabra)
    dar_vuelta(lista)
elif opcionmenu==3:
    print("adios")

