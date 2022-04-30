
    # Exercicio 8 - Lista 2

#   Sabendo que 
#       A=3
#       B=7
#       C=4
#   informe se as expressões abaixo são verdadeiras ou falsas.

A = 3
B = 7
C = 4
'''
    (A + C) > B
    |_____|
       7    > 8
       |______|
           F
'''
print((A + C) > B)



'''
    B >= (A + 2)
         |_____|
    B >=    5
    |_______|
        V   
'''
print(B >= (A + 2))



'''
    C == (B – A)
         |_____|
    C ==    4
    |________|
         V
'''
print(C == (B - A))


'''
    (B + A) <= C
    |_____| <= C
       10   <= C
       |_______|
           F
'''
print((B + A) <= C)


'''
    (C + A) > B
    |_____|
       7    > B
       |______|
           F
'''
print((C + A) > B)


