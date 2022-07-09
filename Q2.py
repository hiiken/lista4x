

ganho = 0
contadorCliente = 0
contadorPromo = 0
contador11 = 0
contador6 = 0
premiacao = 1711
somaValor = 0
clienteMenos = 0


print("valor tent1 tent2 total qmais qsetor6 premio")
while(ganho <= 1711):
    clienteMenos = 0
    ganhoRodada = 0
    valor = int(input())

    if(valor > 296 ):
        dado = int(input())
        dado2 = int(input())
        contadorPromo += 1

        if(dado == 6):
            ganho += 617
            ganhoRodada += 617
            contador6 = contador6 + 1

        if(dado + dado2 >= 11):
            ganho += 1088
            ganhoRodada += 1088
            contador11 += 1

        premiacao -= ganhoRodada
        somaValor += valor

        contadorCliente += 1
       # print("{} {} {} {} {} {} {}".format(valor, dado, dado2, contadorCliente, contador11, contador6, premiacao))
        print(f"{valor: 5} {dado: 5} {dado2: 5} {contadorCliente: 5} {contador11: 5} {contador6: 7} {premiacao: 6}")
      
    else:
        contadorCliente += 1
        clienteMenos += 1
        print(f"{valor: 5} {dado: 5} {dado2: 5} {contadorCliente: 5} {contador11: 5} {contador6: 7} {premiacao: 6}")


x = (contador11/contadorCliente)*100


print("Premio =   1711")
print("Total de participantes =   {}".format(contadorCliente))
print("Quant. clientes gastaram no maximo 296.00 =   {}".format(clienteMenos))
print("Clientes acertaram 6 na 1a tent. =   {}".format(contador6))
print("Porcentagem clientes acertaram mais que 11 =   {:.1f}".format(x))



#print("Premio = 1711\nTotal de participantes = {}\nQuant. clientes gastaram no maximo 296.00 = {}\nClientes acertaram 6 na 1a tent. = {}\nPorcentagem clientes acertaram mais que 11 = {}".format(contadorCliente, clienteMenos, contador6,)
