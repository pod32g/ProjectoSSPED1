from .validar import Validar as v


class Grupos:
    def __init__(self):
        self.primero = None

    def isEmpty(self):
        if self.primero == None:
            return True
        else:
            return False

    def add(self, grupo):
        if self.isEmpty():
            self.primero = grupo
        else:
            h = self.primero
            while not h == None:
                h = h.siguiente
            h = grupo

    def show(self):
        h = self.primero
        while not h == None:
            print(h.nombre + ": ")
            h.show()
            h = h.siguiente

    def getGroup(self, name):
        h = self.primero
        while not h == None and not h.nombre == name:
            h = h.siguiente
        if h == None:
            return "nuevo"
        else:
            return h

    def modify(self, nombre):
        h = self.primero
        while not h == None and not h.nombre == nombre:
            h = h.siguiente

        y = v.s_input("1-Cambiar nombre de grupo\n2-Editar alumno de grupo")
        if y == 1:
            h.nombre = v.s_input("Ingrese el nuevo nombre")
        else:
            print("Alumnos disponibles: ")
            h.show()
            codigo = v.i_input("Ingrese el codigo del alumno a modificar: ")
            if v.v_code(codigo):
                h.modify(codigo)
            else:
                print("Error, codigo invalido")

    def delete(self, nombre):
        h = self.primero
        while not h == None and not h.nombre == nombre:
            h = h.siguiente
        if h.siguiente == None:
            h = None
        elif h == None:
            pass
        else:
            h = h.siguiente.siguiente
