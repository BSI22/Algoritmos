
#  Questao 4 - lista

#  Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse
#  trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. Sabe-se
#  que cada operação bancária de retirada paga CPMF de 0,38% e o saldo inicial 
#  da conta está zerado.


salario = float(input("Informe o valor do seu salário: "))
cheque_1 = float(input("Informe o valor do cheque 1: "))
cheque_2 = float(input("Informe o valor do cheque 2: "))
CPMF = 0.38/100

salario = salario -(cheque_1 + (cheque_1 * CPMF))
print(f"Valor do salario atualizado {salario:.2f}")

salario = salario -(cheque_2 + (cheque_2 * CPMF))
print(f"Valor do salario atualizado {salario:.2f}")