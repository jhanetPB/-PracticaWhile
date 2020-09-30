#ESTUDIANTE: JHANET PARRAGA BLANCO
print("PRIMER EJERCICIO")
print("=====================================================")
n=int(input())
for i in range(0,n):
    x=float(input())
    y=float(input())
    a=float(input())
    b=float(input())
    c=0
    contador =0
    sw=False
    while(c<(a-b)):
        c=c+(x-y)
        if(c<0):
            sw=True
            break
        else:
            contador=contador+1
    if(sw==True):
        print("NO SE RECUPERA")
    else:
        contador = round(contador / 2)
        semana = round(contador / 5)
        dias = round(((contador / 5) - semana) * 5)
        print(semana, "SEMANAS", dias, "DIAS")