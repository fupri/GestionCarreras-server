class User:
    def __init__(self):
        pass
    
    def getUsername(self):
        return self.__username
    
    def setUsername(self, name):
        self.__username = name

    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password