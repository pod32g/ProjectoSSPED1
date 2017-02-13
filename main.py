from alumno import Alumno
from grupo import Grupo
from grupos import Grupos
from validar import Validar as v


def main():
    grupos = Grupos()
    while True:
        m = v.i_input("Menu\n" \
                      "1-Agregar\n" \
                      "2-Mostrar\n" \
                      "3-Modificar\n" \
                      "4-Borrar\n" \
                      "5-Ordenar\n")
        if int(m) == 1:
            name = v.s_input("Ingrese el nombre del grupo: ")
            g = grupos.getGroup(name)
            if g == "nuevo":
                g = Grupo()
                g.nombre = name
                a = None
                while 1 == 1:
                    n = v.s_input("Ingrese nombre de alumno: ")
                    c = v.i_input("Ingrese codigo de alumno: ")
                    cc = v.i_input("Ingrese promedio de alumno: ")
                    a = Alumno(nombre=n, codigo=c, calificacion=cc)
                    g.add(a)
                    if not v.s_input("Desea agregar otro alumno?: ") == "si":
                        break
                grupos.add(g)
            else:
                while 1 == 1:
                    n = v.s_input("Ingrese nombre de alumno: ")
                    c = v.v_code(v.i_input("Ingrese codigo de alumno: "))
                    cc = v.i_input("Ingrese promedio de alumno: ")
                    a = Alumno(nombre=n, codigo=c, calificacion=cc)
                    g.add(a)
                    if not v.s_input("Desea agregar otro alumno?: ") == "si":
                        break
        elif int(m) == 2:
            grupos.show()
        elif int(m) == 3:
            grupos.modify(v.s_input("Ingrese el nombre del grupo: "))
        elif int(m) == 4:
            grupos.delete_from(v.s_input("Ingrese el nombre del grupo: "))
        elif int(m) == 5:
            grupos.sort(v.s_input("Ingrese el nombre del grupo: "))


if __name__ == '__main__':
    main()
