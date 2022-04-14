
#  Questao 6 - lista

#  Uma padaria vende uma certa quantidade de pães franceses e uma quantidade
#  de broas a cada dia. Cada pão custa R$ 0,50 e a broa custa R$ 1,50. Ao 
#  final do dia, o dono quer saber quanto arrecadou com a venda dos pães e
#  broas (juntos), e quanto deve guardar numa conta de poupança (10% do total
#  arrecadado). Faça um algoritmo para ler as quantidades de pães e de broas,
#  e depois calcular os dados solicitados.

quant_pao = int(input("Informe a quantidade de pães: "))
quant_broa = int(input("Informe a quantidade de broa: "))
valor_pao = 0.50
valor_broa = 1.50

total = valor_pao * quant_pao + valor_broa * quant_broa
guardar_poupanca = total * 10 / 100    # ou total * 0,1

print(f'Valor total vendido foi R${total} e precisa guardar R${guardar_poupanca} reais na poupança')
