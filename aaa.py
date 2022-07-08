import random

ganho = 0
contador = 0
contadorPromo = 0
contador11 = 0
contador6 = 0
premiacao = 0


print("valor tent1 tent2 total qmais qsetor6 premio")
while(ganho <= 1711):

    valor = int(input())

    if(valor > 296 ):
        dado = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        contadorPromo += 1

        if(dado == 6):
            ganho += 617
            contador6 += 1

        elif(dado + dado >= 11):
            ganho += 1088
            contador11 += 1

        contador += 1



        print("%5d", contador)

    
