from carreras import Carrera
from user import User
from bddconnection import DBConnection

class CarrerasDAO:
    def __init__(self):
        self.__carrera = Carrera()

    def login(self, user: User):
        dbconnector = DBConnection(user.getUsername(), user.getPassword())
        self.__db = dbconnector.connectToDB()

    def selectAllCarreras(self): 
        with self.__db.cursor() as dbCursor:
            sql = "SELECT * FROM carreras"
            dbCursor.execute(sql)
            tuplaCarreras = dbCursor.fetchall()

            for tupla in tuplaCarreras:
                self.__carrera.setId(tupla[0])
                self.__carrera.setTitulo(tupla[1])
                self.__carrera.setRama(tupla[3])
                self.__carrera.setDuracion(tupla[2])
                self.__carrera.setCampus(tupla[4])
                carreraARR += [self.__carrera]
            
            return carreraARR

    def selectCarreraByID(self, carrera: Carrera):
        with self.__db.cursor() as dbCursor:
            sql = "SELECT * FROM carreras c WHERE c.idCarrera = %s"
            values = (carrera.getId(),)
            dbCursor.execute(sql, values)

            tupla = dbCursor.fetchall()
            self.__carrera.setId(tupla[0])
            self.__carrera.setTitulo(tupla[1])
            self.__carrera.setRama(tupla[3])
            self.__carrera.setDuracion(tupla[2])
            self.__carrera.setCampus(tupla[4])
            return self.__carrera
    
    def modifySelectedCarrera(self, carrera: Carrera):
        with self.__db.cursor() as dbCursor:
            sql = "UPDATE carreras SET Titulo = %s, Duracion = %s, Rama = %s, Campus = %s WHERE idCarrera = %s"
            values = (carrera.getTitulo(), carrera.getDuracion(), carrera.getRama(), carrera.getCampus(), carrera.getId())
            dbCursor.execute(sql, values)
            self.__db.commit()
            return carrera
    
    def insertCarrera(self, carrera: Carrera):
        with self.__db.cursor() as dbCursor:
            sql = "INSERT INTO carreras (Titulo, Duracion, Rama, Campus) VALUES (%s, %s, %s, %s);"
            values = (carrera.getTitulo(), carrera.getDuracion(), carrera.getRama(), carrera.getCampus())
            dbCursor.execute(sql, values)
            self.__db.commit()
            return self.checkRows(dbCursor.rowcount)
    
    def deleteCarrera(self, carrera: Carrera):
        with self.__db.cursor() as dbCursor:
            dbCursor = self.__db.cursor()
            sql = "DELETE FROM carreras WHERE idCarrera = %s"
            values = (carrera.getId(),)
            dbCursor.execute(sql, values)
            self.__db.commit()
            return self.checkRows(dbCursor.rowcount)

    def checkRows(self, count):
        if count > 0:
            return True
        else:
            return False