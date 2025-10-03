from bddAPI import API
from bddconnection import DBConnection
from carreras import Carrera

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
        info = self.__API.selectCarreraByID(id)
        carrera = Carrera(info[1], info[2], info[3], info[4])
        carrera.setId(info[0])
        return carrera
    
    def seleccionaTodas(self):
        carreraARR = []
        carrera = Carrera()
        tuplaCarreras = self.__API.selectAllCarreras()
        for tupla in tuplaCarreras:
            carrera.setId(tupla[0])
            carrera.setTitulo(tupla[1])
            carrera.setRama(tupla[3])
            carrera.setDuracion(tupla[2])
            carrera.setCampus(tupla[4])
            carreraARR += [carrera]
        return carreraARR