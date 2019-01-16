

class MenuOption:
    def __init__(self, message, option):
        self.__message = message
        self.__option = option

    def get_option(self): return self.__option

    def print(self):
        print(self.__message)
