from .validar import Validar as v


class Main():
    def __init__(self):
        pass

    @staticmethod
    def menu() -> int:
        return v.i_input("Menu\n")
