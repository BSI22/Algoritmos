
#  Questao 8 - lista

#  Um restaurante a quilo cobra R$45,00 o Kg de refeição. Escreva um algoritmo
#  que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor
#  a pagar. Lembre-se que deve ser informado o peso do prato (tara), para que 
#  seja descontado do peso total.

prato_cliente = float(input("Informe o peso do prato do cliente: "))
PESO_PRATO = 0.250
valor_kilo = 45

print(f'O valor a ser pago é {(prato_cliente - PESO_PRATO)*valor_kilo}')
