
#  Escreva as expressões algébricas em forma computacional. 
#  Não se preocupe nesse momento em atribuir o resultado da
#  expressão a uma variável.
#      Exemplo: 
#         Expressão: x + vy 
#         Algoritmo: x + v * y

a, b, c, d, x, y = 5, 6, 7, 8, 9, 2

#  Questão a)
''' 
    Expressão: a + bc + d
    Algoritmo: a + b * c + d
'''
print(a + b * c + d)



#  Questão b)
'''
    Expressão: (a+b) c + d (a-2b)
    Algoritmos: (a + b) * c + d * (a - 2 * b)
'''
print((a + b) * c + d * (a- 2 * b))



#  Questão c)
'''
    Expressão: [2a + (c-d)2] 2
    Algoritmos: (2 * a + (c - d) * 2) * 2
'''
print((2 * a + (c - d) * 2) * 2)



#  Questão d)
'''
    Expressão: (x+y) (x-y)
    Algoritmos: x**2 - y**2
'''      
        #  Explicação matematica distributiva: 
        #  https://www.mathway.com/pt/popular-problems/Algebra/203605

print(x**2 - y**2)