import random
i=0
print("BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA")
print("*"*50)
for i in range (0,3):
    choose = random.randint(1,3)
    print("*"*50)

    print("RONDA NUMERO " + str(i+1))
    case = input("Eligiste: ").lower()

    if choose == 1:
        print("La IA elegio piedra")
        choose = "piedra"
    elif choose == 2:
        print("La IA elegio tijeras")
        choose = "tijera"
    elif choose == 3:
        print("La IA elegio papel")
        choose = "papel"
    else:
        print("eleccion equivocada")
    
    if ("piedra" or "tijera" or "papel") == (choose):
        print("EMPATE")
    elif (case == "piedra" and choose == "tijera" ) or (case == "tijera" and choose == "papel" ) or (case == "papel" and choose == "piedra"):
        print("GANASTE")
    else:
        print("PERDISTE")
    print("*"*50)

