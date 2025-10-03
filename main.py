from carreras import Carrera
from gestioncarreras import GestionCarrera

def menu():
    carrera = Carrera()
    gestor = GestionCarrera("root", "123456")

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
            carreras = gestor.seleccionaTodas()
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados.getTitulo()}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a visualizar: ")) - 1]
                if selectedCarrera:
                    print (selectedCarrera)
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")

        elif opcion == 3:
            carreras = gestor.seleccionaTodas()
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados.getTitulo()}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a modificar: ")) - 1]
                if selectedCarrera:
                    print (selectedCarrera)
                    selectedCarrera.setTitulo(input("¿Cómo se llamará a partir de ahora? "))
                    selectedCarrera.setDuracion(int(input("¿Cuanto durará? ")))
                    selectedCarrera.setRama(input("¿A que rama pertenecerá? "))
                    selectedCarrera.setCampus(input("¿Dónde se impartirá? "))
                    gestor.modificaCarrera(selectedCarrera)
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")

        elif opcion == 4:
            carreras = gestor.seleccionaTodas()
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados.getTitulo()}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a eliminar: ")) - 1]
                if selectedCarrera:
                    print (selectedCarrera)
                    gestor.eliminaCarrera(selectedCarrera)
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")
        elif opcion == 5:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    menu()