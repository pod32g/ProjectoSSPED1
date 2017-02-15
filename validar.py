import json
from os import listdir
from os.path import isfile, join


class Validar:
    @staticmethod
    def s_input(message) -> str:
        x = input(message)
        try:
            str(x)
            return x
        except Exception as e:
            print("Error")

    @staticmethod
    def i_input(message) -> int:
        x = input(message)
        try:
            int(x)
            return x
        except Exception as e:
            print("Error")

    @staticmethod
    def v_code(code) -> bool:
        if len(code) > 9:
            return False
        else:
            return True


class Tools():
    '''
    theory says that this will receive a json
    [{ name: 'group', alumni: [{name: 'test', gpa: 'test' }]}]
    '''

    @staticmethod
    def toFile(data, filename):
        with open(filename, 'w+') as file:
            file.write(data)

    @staticmethod
    def fromFile(filename):
        with open(filename) as file:
            return json.load(file)

    @staticmethod
    def getFilesFromDir(dirName):
        # Theory says that this will return all files from a dir using an array
        files = [f for f in listdir(dirName) if isfile(join(dirName, f))]
        return files
