class Piloto:
    def __init__(self):
<<<<<<< HEAD
        self.__nombre= None
        self.__fechaNacimiento= None
        self.__salarioAnual= None
        self.__Pais= None
=======
        self.__nombre = None
        self.__fechaNacimiento = None
        self.__salarioAnual = None
        self.__pais = None
>>>>>>> 52f42c47a78ee7403ca5d5c495820efaaa96d656

    @property
    def nombre(self):
        return self.__nombre
<<<<<<< HEAD
    
    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    
    @property
    def salarioAnual(self):
        return self.__salarioAnual
    
    @property
    def Pais(self):
        return self.__Pais
    
    #get
    
    @nombre.setter
    def nombre (self,dato):
        self.__nombre=dato
        
    @fechaNacimiento.setter
    def fechaNacimiento (self,dato):
        self.fechaNacimiento=dato
        
    @salarioAnual.setter
    def salarioAnual (self,dato):
        self.salarioAnual=dato
        
    @Pais.setter
    def Pais (self,dato):
        self.Pais=dato
=======

    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento

    @fechaNacimiento.setter
    def fechaNacimiento(self, dato):
        self.__fechaNacimiento = dato

    @property
    def salarioAnual(self):
        return self.__salarioAnual

    @salarioAnual.setter
    def salarioAnual(self, dato):
        self.__salarioAnual = dato

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, dato):
        self.__Ppis = dato
>>>>>>> 52f42c47a78ee7403ca5d5c495820efaaa96d656
