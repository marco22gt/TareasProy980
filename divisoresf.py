

def divisores (i):
    a = 0
    divisores = []
    for j in range(1, i ):
        if i % j == 0:
            divisores.append(j)
            a = a + j
            if a == i:
                print ("es número perfecto") 
    print (divisores)
    print ("suma")
    print (a)    
    return divisores

def perfect1 ():
    print ("ingrese su nombre:")
    nombre = input()
    print ("Mealegra conocerle" , nombre)
    return (nombre)




    