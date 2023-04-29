from Piloto import Piloto

<<<<<<< HEAD
class Escuderia:
    def __init__(self):
        self.__nombre= None
        self.__casaMotor= None
        self.__PilotoPrincipal= Piloto()
        self.__Piloto2= Piloto()
        self.__Costos =None
        
    #get 
    
    @property
    def nombre(self):
        return(self.__nombre)
    
    @property
    def casaMotor(self):
        return(self.__casaMotor)
    
    @property
    def PilotoPrincipal(self):
        return(self.__PilotoPrincipal)
    
    @property
    def Piloto2(self):
        return(self.__Piloto2)
    
    @property
    def Costos(self):
        return(self.__Costos)
    
    #set
    
    @nombre.setter
    def nombre (self,dato):
        self.__nombre=dato
        
    @casaMotor.setter
    def casaMotor (self,dato):
        self.casaMotor=dato
        
    @PilotoPrincipal.setter
    def PilotoPrincipal (self,dato):
        self.PilotoPrincipal=dato
        
    @Piloto2.setter
    def Piloto2 (self,dato):
        self.Piloto2=dato
        
    @Costos.setter
    def Costos (self,dato):
        self.Costos=dato
=======

class Escuderia:
    def __init__(self):
        self.__nombre = None
        self.__casaMotor = None
        self.__pilotoPrincipal = Piloto()
        self.__piloto2 = Piloto()
        self.__costos = None

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

    @property
    def casaMotor(self):
        return self.__casaMotor

    @casaMotor.setter
    def casaMotor(self, dato):
        self.__casaMotor = dato

    @property
    def pilotoPrincipal(self):
        return self.__pilotoPrincipal

    @pilotoPrincipal.setter
    def pilotoPrincipal(self, dato):
        self.__pilotoPrincipal = dato

    @property
    def piloto2(self):
        return self.__piloto2

    @piloto2.setter
    def piloto2(self, dato):
        self.__piloto2 = dato

    @property
    def costos(self):
        return self.__costos

    @costos.setter
    def costos(self, dato):
        self.__costos = dato
>>>>>>> 52f42c47a78ee7403ca5d5c495820efaaa96d656
