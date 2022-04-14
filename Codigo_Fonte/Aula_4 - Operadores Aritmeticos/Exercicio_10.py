
#  Questao 10 - lista

#  Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit.
#  Faça um algoritmo para ler uma temperatura Celsius e imprimi-la em Fahrenheit 
#  (pesquise como fazer este tipo de conversão).
''''Formula = C x 1,8 + 32'''

Celsius = float(input("Informe o valor em graus Celcius: "))
fahrenheit = Celsius * 1,8 + 32

print(f'A temperatura é {fahrenheit}°F')
