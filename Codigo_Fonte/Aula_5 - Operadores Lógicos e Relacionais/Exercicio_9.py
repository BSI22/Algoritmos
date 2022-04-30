
    # Exercicio 9 - Lista 2

#   Sabendo que 
#       A=5
#       B=4
#       C=3
#       D=6
#   informe se as expressões abaixo são verdadeiras ou falsas.

A, B, C, D = 5, 4, 3, 6

'''
    (A > C) e (C <= D)
    |_____|
       V    e (C <= D)
              |______|
        V   e    V
        |________|
            V          
'''
print((A > C) and (C <= D))


'''
    (A + B) > 10 ou (A + B) == (C + D)
    |_____|
       9    > 10 ou (A + B) == (C + D)
                    |_____|
       9    > 10 ou    9    == (C + D)
                               |_____|
       9    > 10 ou    9    ==    9
       |_______|
           F     ou    9    ==    9
                       |__________|
           F     ou         V
           |________________|
                    V
'''
print((A + B) > 10 or (A + B) == (C + D))


'''
    (A >= C) e (D >= C)
    |______|
        V    e (D >= C)
               |______|
        V    e     V
        |__________|
             V
'''
print((A >= C) and (D >= C))
