import requests as req

API_URL = "http://127.0.0.1:5000" 

def login():
    print("Bienvenido al gestor de carreras universitarias")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    req.post(f"{API_URL}/login/", json={"username": username, "password": password})

    menu()

def menu():
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
            carrera = {}
            carrera["titulo"] = input("Titulo/Grado: ")
            carrera["duracion"] = int(input("¿Cuantos años? "))
            carrera["rama"] = input("Rama de la carrera: ")
            carrera["campus"] = input("¿En que campus se imparte? ")
                            
            resp = req.post(f"{API_URL}/addCarrera/", json=carrera) 
            print(resp.text)

        elif opcion == 2:
            resp = req.get(f"{API_URL}/selectAll/")
            carreras = resp.json() if resp.ok else []
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados['titulo']}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a visualizar: ")) - 1]
                if selectedCarrera:
                    print (selectedCarrera["titulo"], selectedCarrera["duracion"], selectedCarrera["rama"], selectedCarrera["campus"])
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")

        elif opcion == 3:
            resp = req.get(f"{API_URL}/selectAll/")
            carreras = resp.json() if resp.ok else []
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados['titulo']}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a modificar: ")) - 1]
                if selectedCarrera:
                    newCarrera = {
                        "id": selectedCarrera["id"],
                        "titulo": input("Nuevo titulo: "),
                        "duracion": int(input("Nueva duracion: ")),
                        "rama": input("Nueva rama: "),
                        "campus": input("Nuevo campus: ")
                    }

                    resp = req.put(f"{API_URL}/modifyCarrera/", json=newCarrera)
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")

        elif opcion == 4:
            resp = req.get(f"{API_URL}/selectAll/")
            carreras = resp.json() if resp.ok else []
            indiceC = 1
            if carreras:
                for grados in carreras:
                    print(f"{indiceC}. {grados['titulo']}")
                    indiceC += 1

                selectedCarrera = carreras[int(input("Introduce el índice de la carrera a eliminar: ")) - 1]
                if selectedCarrera:
                    req.delete(f"{API_URL}/deleteCarrera/", params={"id": selectedCarrera["id"]})
                else:
                    print("Está vacío")
            else:
                print("No hay carreras en la base de datos")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
            

if __name__ == "__main__":
    login()