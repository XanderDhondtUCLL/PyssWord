class Pasgenerator:
    def __init__(self):
        self.__length = 12
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value: int):
        self.__length = value

    