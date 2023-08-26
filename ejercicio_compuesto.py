import random 
"""
print ("-----------REGISTRO---------")

print("telefono------->")
telefono=int(input())
print ("correo-------->")
correo=str(input())
print ("contraseña---->")
contrasena=str(input())
capchat=int(16)

print ("--------LOGIN--------")

print("telefono------>")
telefono1=int(input())
print("correo------>")
correo1=str(input())
print ("contraseña---->")
contrasena1=str(input())
print ("Resuelva lo siguient (10*2-4)")
capchat1=int(input())

if telefono==telefono1 or correo==correo1 and contrasena==contrasena1 and capchat==capchat1 :
   print("Bienvenido al sistema de registro")
"""

menu = 1  # Inicializa la variable "menu" para que el bucle funcione

while menu == 1:
    print("*****Menú****")
    print("opción 1------>Juego")
    print("opción 2------>Tarjeta de crédito")
    print("opción 3------>Regresar")

    opcion = int(input())

    if opcion == 1:
        print("***************juego**************")
        vidas = 5
        puntos = 0

        while vidas != 0:
            num = random.randint(0, 9)

            if num == 0:
                vidas -= 1
                print(f"vidas:{vidas}")
            else:
                puntos += 1
                print(f"puntos:{puntos}")

        print("Desea volver al menú principal? si/no")
        volver = input()

        if volver == "si":
            menu = 1  # Vuelve al menú principal
        else:
            menu = 2  # Sal del bucle y finaliza el programa

    elif opcion == 2:
        print("Valor de la compra")
        compra = int(input())

        print("Número de cuotas")
        cuotas = int(input())
        contador = 1
        deuda = compra
        print("*******PLAN DE PAGO*******\n")

        while contador <= cuotas:
            valor = compra / cuotas
            print("cuota---->" + str(contador) + "=" + str(valor))
            contador += 1
            deuda = deuda - valor
            cupo = compra - deuda
            print("El valor de la deuda es: " + str(deuda))
            print("El valor del cupo es: " + str(cupo) + "\n")
            if deuda == 0:
                print("Ha terminado de pagar la deuda\n")
    else:
        print("Revise los datos del usuario")


   

      
      
           











