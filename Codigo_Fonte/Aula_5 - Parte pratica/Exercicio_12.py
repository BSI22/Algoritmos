
    # Questão 12 - Lista 2

#   Elabore um algoritmo que leia o nome e o ano de
#   nascimento de uma pessoa e mostre qual é a sua
#   idade atual. 

nome = input("Digite seu nome: ")
dt_nasc = int(input("Digite seu ano de nascimento: "))

idade = 2022 - dt_nasc

print(f'Parabens {nome} você tem {idade}')





''' ------ Forma muito complexa pro mesmo problema ------ '''

from datetime import date
# Importação da biblioteca de data do python

nome = input("Digite seu nome: ")
dt_nasc = input("Digite sua data de nascimento: ")
number = "1234567890"
dt_list = []
idade = 0
# Criação de variaveis

for indice in range(len(dt_nasc)):
  # laço de repetição usando como base o tamanho da data
  # para percorrermos o a string da data nascimento 
    if not(number.find(dt_nasc[indice]) > -1):
      # verificação se o valor em que o indice está é um numero ou não
      # com base em uma consulta no na string de usando find. Se for 
      # qualquer separador retorna -1 e entra dentro do if.  
        dt_list = dt_nasc.split(dt_nasc[indice])
          # forma de separar os numeros em um vetor sem o seperador
          # assim teremos dia mes e ano em posições diferentes.
        
idade = date.today().year - int(dt_list[2])
  # calculo da idade padrão utilizando como base o ano atual
  # idade = 2022 (biblioteca) - 2001 (inserido pelo usuario)  

if int(dt_list[1]) >= date.today().month:
  # verificação para saber se o mês de aniversario é maior que o atual
  # se for será debitado 1 da idade do usuario
    idade -= 1
    if int(dt_list[0]) < date.today().day:
      # verificação para saber se o dia de aniversario é menor que o atual
      # se for será debitado 1 da idade do usuario
        idade -= 1

if idade >= 0:
  # validacao para saber se a pessoal é maior de 0 anos e ela informou uma idade valida
    print(f'Parabens {nome} você tem {idade}')
else:
    print(f'data de nascimento informada {dt_nasc} é invalidade')