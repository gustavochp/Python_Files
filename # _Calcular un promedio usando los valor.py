# _Calcular un promedio usando los valores ingresados
listaVal=[] # _Creo una lista vacia
valorInp=1  # _Valor para iniciar el while
while valorInp!=0:
    valorInp=int(input("Ingresar un valor para calcular el promedio. (Para terminar ingresar 0): "))
    if valorInp==0:
        print("Se ingreso un 0, se termina la rutina")
    else:
        listaVal.append(valorInp)

# _Verifico si hay valores para calcular
if len(listaVal)>0:
    suma=sum(listaVal)
    promedio=float(suma/len(listaVal))
    print(f"La suma de los valores ingresados es: {suma} y la cantidad de valores es: {len(listaVal)}")
    print(f"El promedio de los valores ingresados es: {promedio:.2f}")
else:
    print("No se ingresaron valores para calcular")
