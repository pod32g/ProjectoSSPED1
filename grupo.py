from validar import Validar as v


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

    def getSize(self):
        h = self.primero
        i = 0
        while not h == None:
            h = h.siguiente
            i += 1
        return i

    def modify(self, codigo):
        h = self.primero
        while not h == None and not h.codigo == codigo:
            h = h.siguiente
        h.nombre = v.s_input("Ingrese Nombre: ")
        h.codigo = v.i_input("Ingrese codigo: ")
        h.calificacion = v.i_input("Ingrese promedio: ")

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
            print(f"\tNombre:   {h.nombre}\n" \
                  f"\tCodigo:   {h.codigo}\n" \
                  f"\tPromedio: {h.calificacion}\n")
            h = h.siguiente

    def getIndex(self, index):
        i = 0
        h = self.primero
        while not i == index:
            if i == index:
                break
            h = h.siguiente
            i += 1
        # print(h)
        return h

    def swapIndex(self, a, b):
        i = 0
        h = self.primero
        while not i == a:
            if i == a:
                break
            h = h.siguiente
            i += 1
        h.nombre = b.nombre
        h.codigo = b.codigo
        h.calificacion = b.calificacion

    def quick(self, low, high):
        i = low
        j = high
        pv = self.getIndex(int((low + high) / 2))

        while i <= j:
            while self.getIndex(i).codigo < pv.codigo:
                i += 1
            while self.getIndex(j).codigo > pv.codigo:
                j -= 1
            if i <= j:
                t = self.getIndex(i)
                self.swapIndex(i, self.getIndex(j))
                self.swapIndex(j, t)
            if low < j:
                self.quick(low, j)
            if i < high:
                self.quick(i, high)
