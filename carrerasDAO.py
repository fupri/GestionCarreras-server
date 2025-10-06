from carreras import Carrera
from bddconnection import DBConnection

class CarrerasDAO:
    def __init__(self, user, password):
        self.__dbconnector = DBConnection(user, password)
        self.__db = self.__dbconnector.connectToDB()
        self.__carrera = Carrera()

    def selectAllCarreras(self):
        dbCursor = self.__db.cursor()
        sql = "SELECT * FROM carreras"
        dbCursor.execute(sql)
        tuplaCarreras = dbCursor.fetchall()
        tuplaCarreras = self.__API.selectAllCarreras()

        for tupla in tuplaCarreras:
            self.__carrera.setId(tupla[0])
            self.__carrera.setTitulo(tupla[1])
            self.__carrera.setRama(tupla[3])
            self.__carrera.setDuracion(tupla[2])
            self.__carrera.setCampus(tupla[4])
            carreraARR += [self.__carrera]
        dbCursor.close()
        
        return carreraARR

    def selectCarreraByID(self, carrera: Carrera):
        dbCursor = self.__db.cursor()

        sql = "SELECT * FROM carreras c WHERE c.idCarrera = %s"
        values = (carrera.getId(),)
        dbCursor.execute(sql, values)

        tupla = dbCursor.fetchall()
        self.__carrera.setId(tupla[0])
        self.__carrera.setTitulo(tupla[1])
        self.__carrera.setRama(tupla[3])
        self.__carrera.setDuracion(tupla[2])
        self.__carrera.setCampus(tupla[4])
        dbCursor.close()

        return self.__carrera
    
    def modifySelectedCarrera(self, carrera: Carrera):
        dbCursor = self.__db.cursor()
        sql = "UPDATE carreras SET Titulo = %s, Duracion = %s, Rama = %s, Campus = %s WHERE idCarrera = %s"
        values = (carrera.getTitulo(), carrera.getDuracion(), carrera.getRama(), carrera.getCampus(), carrera.getId())
        dbCursor.execute(sql, values)
        self.__db.commit()
        dbCursor.close()

        return self.checkRows(dbCursor.rowcount)
    
    def insertCarrera(self, carrera: Carrera):
        dbCursor = self.__db.cursor()
        sql = "INSERT INTO carreras (Titulo, Duracion, Rama, Campus) VALUES (%s, %s, %s, %s);"
        values = (carrera.getTitulo(), carrera.getDuracion(), carrera.getRama(), carrera.getCampus())
        dbCursor.execute(sql, values)
        self.__db.commit()
        dbCursor.close()
        return self.checkRows(dbCursor.rowcount)
    
    def deleteCarrera(self, carrera: Carrera):
        dbCursor = self.__db.cursor()
        sql = "DELETE FROM carreras WHERE idCarrera = %s"
        values = (carrera.getId(),)
        dbCursor.execute(sql, values)
        self.__db.commit()
        dbCursor.close()
        return self.checkRows(dbCursor.rowcount)

    def checkRows(self, count):
        if count > 0:
            return True
        else:
            return False