"""print ("hola  git")
a = [1,2,3,4,5]
print (type(a))
b = ("a","b","c","d","e")
print (type(b))
c = (1,2,3,4,5)
print (type(c))
print (c[0])
print(b[1]) 
     
for i in c:
    print(i)

for j in range(0, 10, 1):
    print (j)
k = 0
while k <= 5:
    
    print(k)
    k += 1
print("Fin")"""

"""Problema 1 de desafío
a = 0
b = 0
c = 0

for i in range(0,1000,1):

    if i % 3 == 0:
        a = 1
    else: 
        a = 0
    if i % 5 == 0:
        b = 1
    else: 
        b = 0
    if a or b == 1:
        c = c + i
        print (c)
"""


#def divisoresls(i):
a = 0
divisores = []
i=28
for j in range(1, i ):
    if i % j == 0:
        divisores.append(j)
        a = a + j
        if a == i:
            print ("es número perfecto") 
           
print (divisores)
print ("suma")
print (a)

print ("ingrese su nombre:")
nombre = input()
print ("Mealegra conocerle" , nombre)    