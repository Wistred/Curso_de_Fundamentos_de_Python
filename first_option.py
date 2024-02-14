import random
stone   = 1
scissor = 2
paper   = 3
i=0

print("BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA")
print("stone   = 1\nscissor = 2\npaper   = 3")
print("*"*50)
for i in range (0,3):
    choose = random.randint(1,3)
    print("*"*50)

    print("RONDA NUMERO " + str(i+1))
    case = int(input("Eligiste: "))

    if choose == 1:
        print("La IA elegio piedra")
    elif choose == 2:
        print("La IA elegio tijeras")
    elif choose == 3:
        print("La IA elegio papel")
    else:
        print("eleccion equivocada")
    
    if case == choose:
        print("EMPATE")
    elif (case == 1 and choose == 2 ) or (case == 2 and choose == 3 ) or (case == 3 and choose == 1):
        print("GANASTE")
    else:
        print("PERDISTE")
    print("*"*50)

