from validar import Validar as v


class Grupos:
    def __init__(self):
        self.primero = None

    def isEmpty(self):
        if self.primero is None:
            return True
        else:
            return False

    def add(self, grupo):
        if self.isEmpty():
            self.primero = grupo
        else:
            h = self.primero
            while h.siguiente is not None:
                h = h.siguiente
            h.siguiente = grupo

    def show(self):
        if self.isEmpty():
            print("No hay nada que mostrar")
            return None

        h = self.primero
        while h is not None:
            print(h.nombre + ": ")
            h.show()
            h = h.siguiente

    def getGroup(self, name):
        h = self.primero
        while h is not None and not h.nombre == name:
            h = h.siguiente
        if h is None:
            return "nuevo"
        else:
            return h

    def modify(self, nombre):
        h = self.primero
        while h is not None and not h.nombre == nombre:
            h = h.siguiente

        y = v.i_input("1-Cambiar nombre de grupo\n2-Editar alumno de grupo\n")
        if int(y) == 1:
            h.nombre = v.s_input("Ingrese el nuevo nombre: ")
        else:
            print("Alumnos disponibles: ")
            h.show()
            codigo = v.i_input("Ingrese el codigo del alumno a modificar: ")
            if v.v_code(codigo):
                h.modify(codigo)
            else:
                print("Error, codigo invalido")

    def delete_from(self, nombre):
        if v.i_input("1-Eliminar grupo\n2-Eliminar alumno\n") == 1:
            self.delete(nombre)
        else:
            h = self.primero
            while h is not None and not h.nombre == nombre:
                print(h)
                h = h.siguiente
            if h is not None:
                h.delete(v.s_input("Ingrese el codigo del alumno: "))
            else:
                print("404 Not Found")

    def delete(self, nombre):
        h = self.primero
        while h is not None and not h.nombre == nombre:
            h = h.siguiente
        if h.siguiente is None:
            h = None
        elif h is None:
            pass
        else:
            h = h.siguiente.siguiente

    def sort(self, nombre):
        h = self.primero
        while h is not None and h.nombre == nombre:
            h = h.siguiente
        if h is not None:
            h.quick(0, h.getSize() - 1)
