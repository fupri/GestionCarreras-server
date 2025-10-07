from flask import Flask, jsonify, request as req
from carrerasDAO import CarrerasDAO
from carreras import Carrera
from user import User

app = Flask(__name__)
DAO = CarrerasDAO()
carrera = Carrera()
user = User()

@app.roue("/login/", ["POST"])
def login():
    user.setUsername(req.args.get('username'))
    user.setPassword(req.args.get('password'))
    DAO.login(user)
    return jsonify({"about": f"logged in correctly, user:" + {user.getUsername()}})

@app.route("/selectAll")
def getAllCarreras():
    carreras = DAO.selectAllCarreras()
    carreras_dict = [carrera.to_dict() for carrera in carreras]
    return jsonify(carreras_dict)

@app.route("/selectCarreraById/")
def getCarreraById():
    id = req.args.get("id")
    carrera.setId(id)
    carrera = DAO.selectCarreraByID(carrera)
    return jsonify(carrera.to_dict)

@app.route("/modifyCarrera/")
def modifyCarrera():
    carrera.setId(req.args.get("id"))
    carrera.setTitulo(req.args.get("titulo"))
    carrera.setDuracion(req.args.get("duracion"))
    carrera.setRama(req.args.get("rama"))
    carrera.setCampus(req.args.get("campus"))
    DAO.modifyCarrera(carrera)
    return jsonify({"about": f"modified carrera: {carrera.getTitulo()}"})

@app.route("/deleteCarrera")
def deleteCarrera():
    carrera.setId(req.args.get("id"))
    DAO.deleteCarrera(carrera)
    return jsonify({"about": f"deleted carrera: {carrera.getTitulo()}"})
    