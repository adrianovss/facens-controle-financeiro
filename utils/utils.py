from configurations.configurations import Configurations

class Utils():
    def __init__(self):
        self.__config = Configurations()

    def read_file(self):
        with open(self.__config.file_output, 'r') as file:
            return list(map(lambda x: x.replace('\n', ''), file.readlines()))


    def write_file(self, _type, value, description):
        with open(self.__config.file_output, 'a+') as file:
            file.write(f'\nOperação: {_type} - Valor: {value} - Descrição: {description}')