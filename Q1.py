for c in range(0 ,13):
    n = int(input())
    if(n % 3 == 0 and n % 5 != 0):
        print("{} é múltiplo de três".format(n))
    elif(n % 3 != 0 and n % 5 == 0):
        print("{} é múltiplo de cinco".format(n))
    elif(n % 3 == 0  and n % 5 == 0):
        print("{} é múltiplo de três e cinco".format(n))
    else:
        print(n)

