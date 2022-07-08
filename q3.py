infiniteLoop = 0

while(infiniteLoop == 0):
    n = float(input())
    if(n > 138):
        print("Meta atingida")
        infiniteLoop = 1
    else:
        print("Insuficiente")
