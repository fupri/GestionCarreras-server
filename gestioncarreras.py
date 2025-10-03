from bddAPI import API

class GestionCarrera:
    def __init__(self):
        self.__API = API()

    def añadeCarrera(self, carrera):
        self.__API.insertCarrera(carrera)

    def eliminaCarrera(self, idCarrera):
        self.__API.deleteCarrera(idCarrera)

    def modificaCarrera(self, carrera):
        self.__API.modifySelectedCarrera(carrera)

    def seleccionaCarrera(self, carrera):
        self.__API.selectCarreraByTitulo(carrera)

    def seleccionaTodas(self):
        self.__API.selectAllCarreras()