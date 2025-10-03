from bddAPI import API
from bddconnection import DBConnection

class GestionCarrera:
    def __init__(self, user, password):
        self.__dbconnector = DBConnection(user, password)
        self.__API = API(self.__dbconnector.connectToDB())

    def añadeCarrera(self, carrera):
        self.__API.insertCarrera(carrera)

    def eliminaCarrera(self, idCarrera):
        self.__API.deleteCarrera(idCarrera)

    def modificaCarrera(self, carrera):
        self.__API.modifySelectedCarrera(carrera)

    def seleccionaCarrera(self, id):
        return self.__API.selectCarreraByID(id)

    def seleccionaTodas(self):
        return self.__API.selectAllCarreras()