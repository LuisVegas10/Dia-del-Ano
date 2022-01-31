'''
Este ejercicio ingreado un numero del 1-365, y dice el dia y mes del año que corresponda.
'''

#Funcion que pide el numero del 1-365, lo validad y si valor es valido lo retorna
def getData():
    isValid = False
    while not isValid: #Un ciclo que se repetira hasta que se ingrese un numero valido
        try:
            nDia = int(input("Ingrese una fecha del año: "))
            if nDia >= 1 and nDia <= 365:
                isValid = True
            elif nDia < 1:
                print("El dia debe ser mayor a 0")
            else:
                print("El dia debe ser menor o igual a 365")
        except Exception as exception:
            print(f"Error: Debe ingresar un numero entero")
    return nDia


#Clase que va a contener el nombre del mes y la cantidad de dias que tiene dicho mes.
class Month(object):
    def __init__(self, name, dias):
        self._Name = name
        self._Dias = dias

#Lista con los 12 meses con su nombre y la cantidad de dia de dicho mes
listMonth = [Month("Enero", 31), Month("Febrero", 28), Month("Marzo", 31), Month("Abril", 30), Month("Mayo", 31), Month("Junio", 30), Month(
    "Julio", 31), Month("Agosto", 31), Month("Septiembre", 30), Month("Octubre", 31), Month("Noviembre", 30), Month("Diciembre", 31)]

dia = getData()
cont = 0
'''
El ciclo ira sumando los dias de los meses en cont, hasta que cont sea mayor a dia.
Si dia <= cont, entonces a cont se resta la misma cantida de dias que se le sumo del mes
A dia se le resta cont y el resutlado es el dia del mes.
El resultado se muestra por consola
'''
for month in listMonth:
    # print(f"Dia: {dia}, Mes {i + 1}: {month._Name}, Dias del mes: {month._Dias}")
    cont += month._Dias
    if dia <= cont:
        cont -= month._Dias
        print(f"{dia - cont} de {month._Name}")
        break
