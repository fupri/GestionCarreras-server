from carreras import Carrera
from gestioncarreras import GestionCarrera
from bddAPI import API

def menu():
    carrera = Carrera()
    gestor = GestionCarrera()

    while True:
        print("""\nMenú Principal
              \n1. Añadir datos
              \n2. Ver datos
              \n3. Actualizar datos
              \n4. Eliminar datos
              \n5. Salir""")
        opcion = int(input("Elige una opcion del menu: "))

        if opcion == 1:
            titulo = input("Titulo/Grado: ")
            duracion = int(input("¿Cuantos años? "))
            rama = input("Rama de la carrera: ")
            campus = input("¿En que campus se imparte? ")
            
            carrera = Carrera(titulo, duracion, rama, campus)
            
            gestor.añadeCarrera(carrera)

        elif opcion == 2:
            carreras = carrera.getGestionCarrera().getResumen()
            if carreras:
                for grados in carreras:
                    print(grados)


                    informacion = carrera.getGestionCarrera().recibeInformacion(id_carrera)
                    if informacion:
                        for dato in informacion:
                            print(informacion)
                    else:
                        print("Está vacío")
            else:
                print("No hay carreras en la base de datos")

        elif opcion == 3:
            print(carrera.getGestionCarrera().getCarreras())
            id_a_modificar = int(input("Introduce el ID de la carrera que quieres modificar: "))
            nuevoTitulo = input("¿Cómo se llamará a partir de ahora? ")
            nuevaDuracion = int(input("¿Cuanto durará? "))
            nuevaRama = input("¿A que rama pertenecerá? ")
            nuevoCampus = input("¿Dónde se impartirá? ")
            carrera = Carrera(nuevoTitulo, nuevaDuracion, nuevaRama, nuevoCampus)
            carrera.getGestionCarrera().modificaInformacion(id_a_modificar, carrera)

        elif opcion == 4:
            id_a_borrar
            carrera.getGestionCarrera().borraDatos(id_a_borrar)

if __name__ == "__main__":
    menu()