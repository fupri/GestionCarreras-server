from carreras import Carrera
from user import User
from bddconnection import DBConnection
from typing import List, Tuple

class CarrerasDAO:
    def __init__(self):
        self.__db = None
        self._user = None
        self._password = None

    def login(self, user: User):
        """Connect to the database and store credentials for reconnection."""
        self._user = user.getUsername()
        self._password = user.getPassword()
        dbconnector = DBConnection(self._user, self._password)
        self.__db = dbconnector.connectToDB()

    def ensure_connection(self):
        """Ensure that the database connection is active, reconnect if not."""
        if not self.__db or not self.__db.is_connected():
            if not self._user or not self._password:
                raise Exception("Database credentials not set. Please login first.")
            dbconnector = DBConnection(self._user, self._password)
            self.__db = dbconnector.connectToDB()

    def selectAllCarreras(self) -> List[Carrera]:
        self.ensure_connection()
        carreraARR: List[Carrera] = []

        with self.__db.cursor(dictionary=True) as dbCursor:
            sql = "SELECT idCarrera, Titulo, Duracion, Rama, Campus FROM carreras"
            dbCursor.execute(sql)
            tuplaCarreras = dbCursor.fetchall()

            if not tuplaCarreras:
                print("No hay carreras en la base de datos (consulta vacía).")
                return []

            for tupla in tuplaCarreras:
                carrera = Carrera()
                carrera.setId(tupla["idCarrera"])
                carrera.setTitulo(tupla["Titulo"])
                carrera.setDuracion(tupla["Duracion"])
                carrera.setRama(tupla["Rama"])
                carrera.setCampus(tupla["Campus"])
                carreraARR.append(carrera)

        return carreraARR

    def selectCarreraByID(self, carrera: Carrera) -> Carrera | None:
        self.ensure_connection()
        with self.__db.cursor() as dbCursor:
            sql = "SELECT idCarrera, Titulo, Duracion, Rama, Campus FROM carreras WHERE idCarrera = %s"
            values = (carrera.getId(),)
            dbCursor.execute(sql, values)
            tupla = dbCursor.fetchone() 

            if not tupla:
                return None

            found = Carrera()
            found.setId(tupla[0])
            found.setTitulo(tupla[1])
            found.setDuracion(tupla[2])
            found.setRama(tupla[3])
            found.setCampus(tupla[4])
            return found

    def modifySelectedCarrera(self, carrera: Carrera):
        self.ensure_connection()
        with self.__db.cursor() as dbCursor:
            sql = "UPDATE carreras SET Titulo = %s, Duracion = %s, Rama = %s, Campus = %s WHERE idCarrera = %s"
            values = (carrera.getTitulo(), carrera.getDuracion(), carrera.getRama(), carrera.getCampus(), carrera.getId())
            dbCursor.execute(sql, values)
            self.__db.commit()
            return carrera

    def insertCarrera(self, carrera: Carrera):
        self.ensure_connection()
        with self.__db.cursor() as dbCursor:
            sql = "INSERT INTO carreras (Titulo, Duracion, Rama, Campus) VALUES (%s, %s, %s, %s)"
            values = (carrera.getTitulo(), carrera.getDuracion(), carrera.getRama(), carrera.getCampus())
            dbCursor.execute(sql, values)
            self.__db.commit()
            return self.checkRows(dbCursor.rowcount)

    def deleteCarrera(self, carrera: Carrera):
        self.ensure_connection()
        with self.__db.cursor() as dbCursor:
            sql = "DELETE FROM carreras WHERE idCarrera = %s"
            values = (carrera.getId(),)
            dbCursor.execute(sql, values)
            self.__db.commit()
            return self.checkRows(dbCursor.rowcount)

    def checkRows(self, count: int) -> bool:
        return count > 0

    def closeConnection(self):
        if self.__db and self.__db.is_connected():
            self.__db.close()
