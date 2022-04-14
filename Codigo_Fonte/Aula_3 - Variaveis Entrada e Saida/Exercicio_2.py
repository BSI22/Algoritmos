
#  Questao 2

#  Declare as seguintes variáveis: nome do funcionario, anoNascimento, numero de
#  filhos, rg, salario, ativo. Atribua valores às respectivas variáveis. A variável
#  ativo deverá receber um valor lógico. Mostre os dados conforme exemplo abaixo:
'''O funcionário <<nome>> com rg <<rg>> possui <<>> anos de vida.
   O salario do funcionario << nome>> é de R$ << salario>> e possui << >> filhos.
   Situação ativo:<<ativo>>'''


nome_1 = "Pedro"
anoNascimento = 2004
numFilhos = 2
rg = 7356941
salario = 2702.54
ativo = True

idade = 2022 - anoNascimento

print(f' O funcionario {nome_1} com rg {rg} possui {idade} anos de vida. \n O salario do funcoinario {nome_1} é de R$ {salario} e possui {numFilhos} filhos. \n Situação {ativo}')