from Escuderia import Escuderia

escuderias=[]

numeroEscuderias = int(input('Digita el numero de escuderias: '))
contador=1
while contador <= numeroEscuderias:
    escuderia = Escuderia()
    escuderia.nombre=input('Digite el nombre de la escuderia: ')
    escuderia.casaMotor=input('Digite el nombre del motor: ')
    escuderia.PilotoPrincipal.nombre=input('Digite el nombre del piloto: ')
    escuderia.PilotoPrincipal.fechaNacimiento=input('Digite la fecha del piloto: ')
    escuderia.PilotoPrincipal.Pais=input('Digite el pais de origen')
    escuderia.PilotoPrincipal.salarioAnual=int(input('Digite el salario...'))
    escuderia.Piloto2.nombre=input('Digite el nombre del piloto: ')
    escuderia.Piloto2.fechaNacimiento=input('Digite la fecha del piloto: ')
    escuderia.Piloto2.Pais=input('Digite el pais de origen')
    escuderia.Piloto2.salarioAnual=int(input('Digite el salario...'))
    
    escuderias.append(escuderia)
    
    contador +=1

#RECORRIENDOLALISTA DE ESCUDERIAS

for escuderia in escuderias:
    print(escuderia.nombre, escuderia.Costos)
    
costoMayor=0
nombreEscuderiaMascara=None
for escuderia in escuderias:
    if escuderia.Costos > costoMayor:
        costoMayor=escuderia.Costo
        