class Carrera:
    def __init__(self, titulo="", duracion=0, rama="", campus=""):
        self.__id = 0
        self.__titulo = titulo
        self.__duracion = duracion
        self.__rama = rama
        self.__campus = campus

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getTitulo(self):
        return self.__titulo
    
    def setDuracion(self, duracion):
        self.__duracion = duracion

    def getDuracion(self):
        return self.__duracion
    
    def setRama(self, rama):
        self.__rama = rama

    def getRama(self):
        return self.__rama
    
    def setCampus(self, campus):
        self.__campus = campus

    def getCampus(self):
        return self.__campus
    
    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def __str__(self):
        return f"{self.__titulo}, duración: {self.__duracion} años, rama: {self.__rama}, campus: {self.__campus}"