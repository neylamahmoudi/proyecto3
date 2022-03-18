numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
preguntar = True

while preguntar == True:
    preguntar = False

    print ("Ingrese el tipo de operacion que desea realizar tomando en cuenta que: Primer valor (+,-,*,/) Segundo valor")
    tipoOperacion = input("Ingrese 1 para sumar, 2 para restar, 3 para multiplicar o 4 para dividir : ")

    if tipoOperacion != "1" and tipoOperacion != "2" and tipoOperacion != "3" and tipoOperacion != "4":
        print ("El tipo de operacion ingresado no es valido")
        preguntar = True

if tipoOperacion == "1":
    print ("El resultado de la suma es: ", numero1+numero2)
elif tipoOperacion == "2":
    print ("El resultado de la resta es: ", numero1-numero2)
elif tipoOperacion == "3":
    print ("El resultado de la mutiplicacion es: ", numero1*numero2)
elif tipoOperacion == "4":
    if numero2 == 0:
        print ("No se puede dividir entre cero")
    else:
        print ("El resultado de la division es: ", numero1/numero2)