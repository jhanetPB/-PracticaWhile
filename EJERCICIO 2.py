#ESTUDIANTE: JHANET PARRAGA BLANCO
print("SEGUNDO EJERCICIO")
print("=====================================================")
n=int(input())
s=1
while(n>0):
    j=n
    suma=0
    while(j>0):
        suma=suma+s
        j=j-1
    s=suma
    n=n-1
print("El factorial es:",s)