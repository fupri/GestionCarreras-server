class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def getUsername(self):
        return self.__username
    
    def setUsername(self, name):
        self.__username = name

    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password