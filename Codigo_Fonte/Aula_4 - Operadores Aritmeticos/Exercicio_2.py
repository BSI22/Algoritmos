
#  Questao 2 - lista

#  Faça um programa que receba o valor de um depósito e o valor da taxa 
#  de juros anual, calcule e mostre o valor do rendimento e o valor total
#  depois do rendimento (após 1 ano);


deposito = float(input("Informe o valor do deposito realizado: "))
taxa_juros = float(input("Informe o valor da taxa de juros anual: "))

rendimento = deposito * taxa_juros / 100 

print(f'O rendimento foi de {rendimento} totalizando um valor de {deposito + rendimento}')
