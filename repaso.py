#numeroUno = int(input('digitalice el primer numero: '))
#numeroDos = int(input('digitalice el segundo numero: '))

#if(numeroUno > numeroDos):
#    print('El numero',numeroUno, 'es mayor que el numero ',numeroDos)
#else:
#    print('El numero',numeroDos, 'es mayor que el numero ',numeroUno)

#LAMBDA UNO
saludar2 = lambda nombre3:f'hola hijo mio como te llamas, {nombre3}'
print(saludar2('Mathias'))


#LAMBDA DOS
suma = lambda a,b: a+b
print('La suma es igual a: ',suma(5, 6))
print('La suma es igual a: ',suma(5, 66))

#LAMBDA TRES

maximo = lambda a, b, c: max(a,b,c)
print('El maximo de numero es: ',maximo(8,50,7))

#LAMBDA CUATRO

def ponerPrefijo(prefijo):
    return lambda nombre: f'{prefijo} {nombre}'

addMr = ponerPrefijo('Mr')
addSr = ponerPrefijo('Sr')
addMiss = ponerPrefijo('Miss')

print(addMr('Anderson'))
print(addSr('Andres'))
print(addMiss('Alejandra'))

#LAMBDA CINCO
def elevarA(exponente):
    return lambda base: base**exponente

elevarCuadrado = elevarA(2)
elevarCubo = elevarA(3)

print(elevarCuadrado(3))
print(elevarCubo(2))

#LAMBDA SEIS

#d1=int(input('Primer numero: '))
#d2=int(input('Segundo numero: '))

#def datos(d1,d2):
#    return lambda rec: rec(d1 * d2)

#multiplo = datos(5,6)

#print(multiplo(5,6,7))

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite El segundo numero: "))

calcularnumeromayor = lambda numero1, numero2 : 1 if numero1>numero2 else -1
mostrarResultado = lambda numero : print("El primer número es mayor",numero1) if numero == 1 else print("El segundo número es mayor",numero2)

mostrarResultado(calcularnumeromayor(numero1, numero2))
