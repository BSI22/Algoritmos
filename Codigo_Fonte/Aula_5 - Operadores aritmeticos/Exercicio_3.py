
    # Exercicio 3 - Lista 2

#   Considere as variáveis abaixo declaradas: 
#      inteiro d, y, p, q,r;
#      real a, b, c, s, z;

#   Indique qual o resultado das expressões aritméticas, onde

a = float(3.0)
b = float(2.0)
c = float(0.5) 
s = float(9.0)
z = float(12.0)
d = int(16)
y = int(2)
p = int(4)
q = int(6)
r = int(24)
x = int(2)


# Questão A
'''
    a)  x + y – z * a
               |_____|
        x + y -  36
       |_____|
          4   - 36
         |________|
            -32
'''
print(x + y - z * a)


# Questão B
''' b)  d / y 
       |_____|
          8
'''
print(d / y)


# Questão C
''' c)  y % d 
       |_____|
          2
    
'''
print(y %  d)


# Questão D
''' d)  p * (r % q) – q / 2 
           |______|
        p *   0     - q / 2
       |_______| - q / 2
           0     - q / 2
                  |_____|
              0  -   3
             |________|
                 -3
'''
print(p * (r % q) - q / 2)


# Questão E
''' e)  (a - b * y - d) 
            |_____|
        (a -   4   - d)
        |_______|
            -1   - d
           |________|
              -17  
'''
print((a - b * y - d))


#Questão F
''' f)  ((z/a) + b * a) – d 
         |____|
        (  4   + b * a) - d
                |_____|
        (  4   +   6)   - d
        |____________|
               10      - d
               |__________| 
                    -6        
'''
print(((z/a) + b * a) - d )
