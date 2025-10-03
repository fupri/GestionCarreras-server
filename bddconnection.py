import mysql.connector

class DBConnection:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password
    
    def connectToDB(self):
        return mysql.connector.connect(
            host="localhost",
            user=self.__user,
            password=self.__password,
            database="gestion_de_carreras"
        )