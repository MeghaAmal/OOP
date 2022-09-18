class CellPhone:
    def __init__(self,man,mod,price):
        self.__manfact = man
        self.__model = mod
        self.__price = price

    def set_manufact(self,man):
        self.__manfact = man

    def set_price(self,price):
        self.__price = price

    def set_model(self,mod):
        self.__model = mod
    
    def get_manufact(self):
        return self.__manfact

    def get_price(self):
        return self.__price

    def get_model(self):
        return self.__model

       