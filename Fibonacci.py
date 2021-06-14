while True:

    n=int(input("Digite quantos termos você quer: "))
    x1=0
    x2=1
    if(n==1):
        print(x1)
    else:
        print(x1)
        print(x2)
    cont=3
    while cont<=n:
        x3=x1+x2
        print(x3)
        x1=x2
        x2=x3
        cont+=1    
