from .validar import Validar as v


class Grupo:
    def __init__(self, nombre=None, siguiente=None):
        self.nombre = nombre
        self.primero = None
        self.siguiente = siguiente

    def add(self, alumno):
        if self.primero == None:
            self.primero = alumno
        else:
            h = self.primero
            while not h.siguiente == None:
                h = h.siguiente
            h.siguiente = alumno

    def modify(self, codigo):
        h = self.primero
        while not h == None and not h.codigo == codigo:
            h = h.siguiente
        h.nombre = v.s_input("Ingrese Nombre")
        h.codigo = v.v_code(v.i_input("Ingrese codigo"))
        h.calificacion = v.i_input("Ingrese promedio")

    def delete(self, codigo):
        h = self.primero
        while not h == None and not h.codigo == codigo:
            h = h.siguiente

        if h.siguiente == None:
            h = None
        elif h == None:
            pass
        else:
            h = h.siguiente.siguiente

    def show(self):
        h = self.primero
        while not h == None:
            print(h.nombre)
            print(h.codigo)
            print(h.calificacion)
            h = h.siguiente
