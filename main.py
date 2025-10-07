from flask import Flask
import requests as req

def login():
    print("Bienvenido al gestor de carreras universitarias")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    menu(user, password)

def menu(user, password):
    carrera = {
        "ID": 0,
        "Titulo": "",
        "Duracion": 0,
        "Rama": "",
        "Campus": ""
    }

    while True:
        print("""\nMenú Principal
              \n1. Añadir datos
              \n2. Ver datos
              \n3. Actualizar datos
              \n4. Eliminar datos
              \n5. Salir""")
        opcion = int(input("Elige una opcion del menu: "))

        if opcion == 1: 
            carrera["Titulo"] = input("Titulo/Grado: ")
            carrera["Duracion"] = int(input("¿Cuantos años? "))
            carrera["Rama"] = input("Rama de la carrera: ")
            carrera["Campus"] = input("¿En que campus se imparte? ")
                        
            resp = req.post("http://localhost:5000/addCarrera/", carrera)
            print(resp.text)

        elif opcion == 2:
            resp = req.post("http://localhost:5000/getAllCarreras/")
            carreras = resp.json() if resp.ok else []
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados['Titulo']}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a visualizar: ")) - 1]
                if selectedCarrera:
                    print (selectedCarrera["Titulo"], selectedCarrera["Duracion"], selectedCarrera["Rama"], selectedCarrera["Campus"])
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")

        elif opcion == 3:
            resp = req.post("http://localhost:5000/getAllCarreras/")
            carreras = resp.json() if resp.ok else []
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados['Titulo']}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a modificar: ")) - 1]
                if selectedCarrera:
                    selectedCarrera["Titulo"] = input("¿Cómo se llamará a partir de ahora? ")
                    selectedCarrera["Duracion"] = int(input("¿Cuanto durará? "))
                    selectedCarrera["Rama"] = input("¿A que rama pertenecerá? ")
                    selectedCarrera["Campus"] = input("¿Dónde se impartirá? ")
                    req.post("http://localhost:5000/updateCarrera/", selectedCarrera)
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")

        elif opcion == 4:
            resp = req.post("http://localhost:5000/getAllCarreras/")
            carreras = resp.json() if resp.ok else []
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados['Titulo']}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a eliminar: ")) - 1]
                if selectedCarrera:
                    req.post("http://localhost:5000/deleteCarrera/", selectedCarrera)
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
            

if __name__ == "__main__":
    login()