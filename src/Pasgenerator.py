import string
import secrets

class Pasgenerator:
    def __init__(self):
        self.__length = 12
        self.__pasword = ''
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value: int):
        self.__length = value

    @property
    def password(self):
        return self.__pasword

    def generate(self):
        # TODO
        # [x] generation of first character
        # [ ] logic to decide which next character of password will be.

        # generate the first character of the password.
        self.__pasword = ''.join(secrets.choice(string.ascii_letters + string.digits)) 
        for i in range(self.__length):
            pass
    