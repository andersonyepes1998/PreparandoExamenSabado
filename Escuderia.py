from Piloto import Piloto

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