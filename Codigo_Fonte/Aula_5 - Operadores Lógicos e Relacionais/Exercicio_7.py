
    # Exercicio 7 - Lista 2

#   Determine os resultados obtidos na avaliação das expressões lógicas seguintes. 
#       x * x + y > z
#       x * x + y > z

#   Considere que os valores iniciais das variáveis são:
#     a) x = 1, y = 2, z = 5
#     b) x = 4, y = 3, z = 1

'''
    x * x + y > z
   |_____|
      1   + y > z
     |_______|
         3    > z
        |_______|
            F
'''
x, y, z = 1, 2, 5
print(x * x + y > z)



'''
    x * x + y > z
   |_____|
      8   + y > z
     |_______|
         11   > z
        |________|
             V
'''
x, y, z = 4, 3, 1
print(x * x + y > z)