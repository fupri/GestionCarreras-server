from bddAPI import API

class GestionCarrera:
    def __init__(self):
        pass

    def añadeCarrera(self, carrera):
        API.insertCarrera(carrera)

    def eliminaCarrera(self, idCarrera):
        API.deleteCarrera(idCarrera)

    def modificaCarrera(self, carrera):
        API.modifySelectedCarrera(carrera)

    def seleccionaCarrera(self, carrera):
        API.selectCarreraByTitulo(carrera)

    def seleccionaTodas(self):
        API.selectAllCarreras()