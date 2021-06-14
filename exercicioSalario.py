salario=float(input("Digite um valo inicial do salario Bruto $: "))
if (salario < 1903.98):
    print("\n Insento de Dedução ")
    print ("\nO salario liquido é:",salario)

while True:

    salario1=float(input("\nDigite um valor de aumento (em reais) para o salario $: "))
    resultado = salario + salario1
    if (resultado < 1903.98):
       print("\n Insento de Dedução ")
       print ("\nO salario liquido é:",salario)
    elif (resultado >= 1903.98 and resultado <= 2826.65):
       print("\nDedução de 7,5%")
       print("\n Seu salario com o desconto [IR] é de $:", resultado - (resultado * 0.075))
    elif (resultado >= 2826.65 and resultado <= 3751.60):
      print("\nDedução de 15%")
      print("\nSeu salario com o desconto [IR] è de $:", resultado- (resultado * 0.15))
    elif(resultado >= 3751.60  and resultado<= 4664.68):
      print("\nDedução de 22,5%")
      print("\nSeu salario com o desconto [IR] è de $:",resultado- (resultado * 0.225))
    elif(resultado >= 4664.68):
      print("\nDedução de 27,5%")
      print("\nSeu salario com o desconto [IR] è de $:", resultado -(resultado * 0.275))
    
