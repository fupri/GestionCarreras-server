from flask import Flask, jsonify, request as req
from carrerasDAO import CarrerasDAO
from carreras import Carrera
from user import User

app = Flask(__name__)
DAO = CarrerasDAO()


@app.route("/login/", methods=["GET"])
def login():
    user = User()
    user.setUsername(req.args.get('username'))
    user.setPassword(req.args.get('password'))
    DAO.login(user)
    return jsonify({"about": f"logged in correctly, user: {user.getUsername()}"})


@app.route("/selectAll/", methods=["GET"])
def getAllCarreras():
    carreras = DAO.selectAllCarreras() or []
    carrerasList = [c.to_dict() for c in carreras]
    return jsonify(carrerasList)


@app.route("/selectCarreraById/", methods=["GET"])
def getCarreraById():
    id_str = req.args.get("id")
    if not id_str:
        return jsonify({"error": "id parameter required"}), 400
    try:
        idv = int(id_str)
    except ValueError:
        return jsonify({"error": "id must be an integer"}), 400

    c = Carrera()
    c.setId(idv)
    found = DAO.selectCarreraByID(c)
    if not found:
        return jsonify({}), 404
    return jsonify(found.to_dict())


@app.route("/addCarrera/", methods=["POST"])
def insertCarrera():
    data = req.get_json() or {}
    # support form-like args as fallback
    if not data:
        data = {k: req.args.get(k) for k in ("titulo", "duracion", "rama", "campus")}

    titulo = data.get("titulo")
    duracion = data.get("duracion")
    if duracion is not None:
        try:
            duracion = int(duracion)
        except Exception:
            return jsonify({"error": "duracion must be integer"}), 400

    if not titulo or duracion is None:
        return jsonify({"error": "titulo and duracion are required"}), 400

    c = Carrera(titulo, duracion, data.get("rama") or "", data.get("campus") or "")
    ok = DAO.insertCarrera(c)
    if not ok:
        return jsonify({"error": "insert failed"}), 500
    return jsonify({"about": f"inserted carrera: {c.getTitulo()}"}), 201


@app.route("/modifyCarrera/", methods=["PUT"])
def modifySelectedCarrera():
    data = req.get_json() or {}
    id_str = data.get("id") or req.args.get("id")
    if not id_str:
        return jsonify({"error": "id required"}), 400
    try:
        idv = int(id_str)
    except Exception:
        return jsonify({"error": "id must be integer"}), 400

    carrera = Carrera()
    carrera.setId(idv)
    existing = DAO.selectCarreraByID(carrera)
    if not existing:
        return jsonify({}), 404

    if "titulo" in data:
        existing.setTitulo(data["titulo"])
    if "duracion" in data:
        try:
            existing.setDuracion(int(data["duracion"]))
        except Exception:
            return jsonify({"error": "duracion must be integer"}), 400
    if "rama" in data:
        existing.setRama(data["rama"])
    if "campus" in data:
        existing.setCampus(data["campus"])

    DAO.modifySelectedCarrera(existing)
    return jsonify({"about": f"modified carrera: {existing.getTitulo()}"})


@app.route("/deleteCarrera/", methods=["DELETE"])
def deleteCarrera():
    id_str = req.args.get("id")
    if not id_str:
        return jsonify({"error": "id required"}), 400
    try:
        idv = int(id_str)
    except Exception:
        return jsonify({"error": "id must be integer"}), 400

    carrera = Carrera()
    carrera.setId(idv)
    existing = DAO.selectCarreraByID(carrera)
    if not existing:
        return jsonify({}), 404

    ok = DAO.deleteCarrera(existing)
    if not ok:
        return jsonify({"error": "delete failed"}), 500
    return jsonify({"about": f"deleted carrera: {existing.getTitulo()}"})
    
@app.teardown_appcontext
def close_db_connection(exception):
    DAO.closeConnection()