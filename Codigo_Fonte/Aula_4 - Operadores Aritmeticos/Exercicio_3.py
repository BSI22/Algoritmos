
#  Questao 3 - lista

#  Sabe-se que:
#      1 Pé =12 polegadas
#      1 jarda = 3 pés
#      1 milha = 1.760 jardas
#  Faça um programa que receba uma medida em pés, faça as conversões e a seguir mostre os resultados em:
#  Polegadas, Jardas e Milhas.


medida_pes = float(input("Informe o valor da medidade em pés: "))
medida_polegadas = 0
medida_jarda = 0
medida_milhas = 0

medida_polegadas = medida_pes * 12

medida_jarda = medida_pes / 3

medida_milhas = medida_jarda / 1760

print(f'O valor {medida_pes} em pés equivale a: ')
print(f'  {medida_polegadas} polegadas')
print(f'  {medida_jarda} jardas')
print(f'  {medida_milhas} milhas')
