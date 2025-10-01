import mysql.connector

class API:
    def __init__(self):
        self.__db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="gestion_de_carreras"
        )

    def selectAllCarreras(self):
        dbCursor = self.__db.cursor()
        sql = "SELECT * FROM carreras"
        dbCursor.execute(sql)
        returnObj = dbCursor.fetchall()
        dbCursor.close()
        return returnObj

    def selectCarreraByTitulo(self, obj):
        dbCursor = self.__db.cursor()
        sql = "SELECT * FROM carreras c WHERE c.Titulo = %s"
        values = obj.Titulo
        dbCursor.execute(sql, values)
        returnObj = dbCursor.fetchall()
        dbCursor.close()
        return returnObj
    
    def modifySelectedCarrera(self, obj):
        dbCursor = self.__db.cursor()
        sql = "UPDATE carreras SET Titulo = %s, Duracion = %s, Rama = %s, Campus = %s WHERE idCarrera = %s"
        values = (obj.id)
        dbCursor.execute(sql, values)
        self.__db.commit()
        dbCursor.close()

        return self.checkRows(dbCursor.rowcount())
    
    def insertCarrera(self, obj):
        dbCursor = self.__db.cursor()
        sql = "UPDATE carreras SET Titulo = %s, Duracion = %s, Rama = %s, Campus = %s WHERE idCarrera = %s"
        values = (obj.id)
        dbCursor.execute(sql, values)
        self.__db.commit()
        dbCursor.close()
        return self.checkRows(dbCursor.rowcount())
        
    def checkRows(self, count):
        if count > 0:
            return True
        else:
            return False 

