'''
Este ejercicio ingreado un numero del 1-365, y dice el dia y mes del año que corresponda.
'''


# DONE: Esta funcion pide un numero del 1-365, el numero es validado y si numero es valido lo retorna
def getDay():
    while True:  # Un ciclo que se repetira hasta que se ingrese un numero valido
        try:
            day = int(input("Ingrese una fecha del año: "))
            if day >= 1 and day <= 365:
                break
            elif day < 1:
                print("¡¡EL DÍA DEBE SER MAYOR A 0!!")
            else:
                print("¡¡EL DÍA DEBE SER MENOR O IGUAL A 365!!")
        except Exception as exception:
            print("¡¡ERROR: DEBE INGRESAR UN NUMERO ENTERO!!")
    return day


# Clase que va a contener el nombre del mes y la cantidad de dias que tiene dicho mes.
class Month(object):
    def __init__(self, name, days):
        self._Name = name
        self._Days = days


# Lista con los 12 meses con su nombre y la cantidad de dia de dicho mes
listMonth = [Month("Enero", 31), Month("Febrero", 28), Month("Marzo", 31), Month("Abril", 30),
             Month("Mayo", 31), Month("Junio", 30), Month("Julio", 31), Month("Agosto", 31), Month("Septiembre", 30), Month("Octubre", 31), Month("Noviembre", 30), Month("Diciembre", 31)]

nDay = getDay()
cont = 0

# El ciclo ira realizando la sumatoria de los dias de los meses en 'cont', hasta que 'cont' sea mayor o igual a 'nDay'. Si 'nDay' es mayor o igual a 'cont', entonces a 'cont' se resta la misma cantida de dias que se le haya sumado del mes. Entonces a 'nDay' se le resta 'cont' y el resutlado es el dia del mes. El resultado se muestra por consola
for month in listMonth:
    cont += month._Days
    if nDay <= cont:
        cont -= month._Days
        print(f"El numero {nDay} es la fecha {nDay - cont} de {month._Name}")
        break
