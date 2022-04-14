
#  Questao 9 - lista

#  Construa um algoritmo para calcular a distância entre dois pontos do
#  plano cartesiano. Cada ponto é um par ordenado (x,y).
''''Formula = √(x2-x1)² + (y2-y1)²'''

print (" - Ponto 1 ")
x1 = float(input("Digite o valor de x do ponto 1: "))
y1 = float(input("Digite o valor de y do ponto 1: "))

print (" ")
print (" - Ponto 2 ")
x2 = float(input("Digite o valor de x do ponto 2: "))
y2 = float(input("Digite o valor de y do ponto 1: "))

distancia = (((x2-x1)**2) + ((y2-y1)**2))**(0.5)

print(f'A distancia entre os pontos é {distancia}')