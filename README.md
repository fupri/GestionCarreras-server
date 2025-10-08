**Requirements**
- Python 3.10+
- MySQL Server running locally (default: localhost, port: 5000
- The following libraries
```
pip install flask mysql-connector-python requests
```

**How to run the app**

_1. Start the Flask Server_

Run the API from a terminal:
```
python api.py
```

_2. Run the Client_

In another terminal (same folder):
```
python main.py
```

You’ll be prompted to log in (use your MySQL username and password).
Then a menu will appear with options like:

1. Añadir carrera
2. Mostrar carreras
3. Modificar carrera
4. Eliminar carrera

and

5. Salir

Each option communicates with the Flask API.



**IMPORTANT!**

Run the server before you run the client
