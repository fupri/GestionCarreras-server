from carreras import Carrera

class API:
    def __init__(self, connector):
        self.__db = connector

    def selectAllCarreras(self):
        dbCursor = self.__db.cursor()
        sql = "SELECT * FROM carreras"
        dbCursor.execute(sql)
        returnObj = dbCursor.fetchall()
        dbCursor.close()
        return returnObj

    def selectCarreraByID(self, carrera: Carrera):
        dbCursor = self.__db.cursor()
        sql = "SELECT * FROM carreras c WHERE c.idCarrera = %s"
        values = carrera.getId()
        dbCursor.execute(sql, values)
        returnObj = dbCursor.fetchall()
        dbCursor.close()
        return returnObj
    
    def modifySelectedCarrera(self, carrera: Carrera):
        dbCursor = self.__db.cursor()
        sql = "UPDATE carreras SET Titulo = %s, Duracion = %s, Rama = %s, Campus = %s WHERE idCarrera = %s"
        values = (carrera.getTitulo(), carrera.Duracion, carrera.Rama, carrera.Campus, carrera.ID)
        dbCursor.execute(sql, values)
        self.__db.commit()
        dbCursor.close()

        return self.checkRows(dbCursor.rowcount())
    
    def insertCarrera(self, carrera: Carrera):
        dbCursor = self.__db.cursor()
        sql = "INSERT INTO carreras (Titulo, Duracion, Rama, Campus) VALUES (%s, %s, %s, %s);"
        values = (carrera.getTitulo(), carrera.getDuracion(), carrera.getRama(), carrera.getCampus())
        dbCursor.execute(sql, values)
        self.__db.commit()
        dbCursor.close()
        return self.checkRows(dbCursor.rowcount)
    
    def deleteCarrera(self, carrera):
        dbCursor = self.__db.cursor()
        sql = "DELETE * FROM carreras WHERE idCarrera = %s"
        values = (carrera.getId(),)
        dbCursor.execute(sql, values)
        self.__db.commit()
        dbCursor.close()
        return self.checkRows(dbCursor.rowcount())

    def checkRows(self, count):
        if count > 0:
            return True
        else:
            return False