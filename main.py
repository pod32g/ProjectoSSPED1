from grupo import Grupo
from grupos import Grupos
from .validar import Validar as v


def menu():
    return v.i_input("Menu\n")


def main():
    grupos = Grupos()
    if menu() == 1:
        name = v.s_input("Ingrese el nombre del grupo: ")
        if grupos.getGroup(name) == "nuevo":
            g = Grupo()
            g.nombre = name
            # Me sigue dando flojera terminar el menu :v
