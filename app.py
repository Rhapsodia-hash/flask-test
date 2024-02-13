from flask import Flask, json, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)


def connect_db():
  host = "b2jvfbwwzwgru1w4egfx-mysql.services.clever-cloud.com"
  database = "b2jvfbwwzwgru1w4egfx"
  user = "umpbhpsayjpkxxrn"
  password = "MPQecUPZwyGfZ922o8wV"
  port = 3306
  try:
    connection = mysql.connector.connect(host=host,
                                         database=database,
                                         user=user,
                                         password=password,
                                         port=port)
  except mysql.connector.Error as err:
    print(f"Error de conexión: {err}")
  else:
    print("Conectado a la base de datos MySQL")
    return connection


@app.route("/get_members", methods=["GET"])
def get_all_members():
  db = connect_db()
  cursor = db.cursor()
  #all_members_param = request.args.get("all", "false")
  id_servidor = request.args.get("id_servidor", None)
  id_usuario = request.args.get("id_usuario", None)
  counts = request.args.get("mount", "false")
  print(type(id_usuario))
  if (id_servidor is not None and id_servidor.isdigit()):
    select_sql = "SELECT * FROM Usuarios;"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    result_dicts = [dict(zip(cursor.column_names, row)) for row in rows]
    result_json = json.dumps(result_dicts)
    db.close()
    if counts.lower() == "true":
      dicter = {"count": len(result_dicts)}
      json_re = json.dumps(dicter)
      return json_re
    return result_json
  elif id_usuario is not None and id_usuario.isdigit():
    select_sql = "SELECT * FROM Usuarios WHERE id_usuario = %s;"
    cursor.execute(select_sql, (int(id_usuario), ))
    rows = cursor.fetchall()
    result_dicts = [dict(zip(cursor.column_names, row)) for row in rows]
    result_json = json.dumps(result_dicts)
    db.close()
    return result_json
  else:
    db.close()
    return jsonify({
        "error":
        "No se proporcionó el parámetro 'id_usuario' o 'id_servidor'."
    })


@app.route("/get_server", methods=["GET"])
def get_all_servers():
  db = connect_db()
  cursor = db.cursor()
  all_servers = request.args.get("all", "false")
  id_server = request.args.get("id_server", None)
  counts = request.args.get("mount", "false")
  if all_servers.lower() == "true":
    select_sql = "SELECT * FROM Servidores;"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    result_dicts = [dict(zip(cursor.column_names, row)) for row in rows]
    result_json = json.dumps(result_dicts)
    db.close()
    if counts.lower() == "true":
      dicter = {"count": len(result_dicts)}
      json_re = json.dumps(dicter)
      return json_re
    return result_json
  elif id_server is not None and id_server.isdigit():
    select_sql = "SELECT * FROM Servidores WHERE id_servidor = %s;"
    cursor.execute(select_sql, (int(id_server), ))
    rows = cursor.fetchall()
    result_dicts = [dict(zip(cursor.column_names, row)) for row in rows]
    result_json = json.dumps(result_dicts)
    db.close()
    return result_json
  else:
    return "Faile"


@app.route("/get_message", methods=["GET"])
def get_all_messages():
  db = connect_db()
  cursor = db.cursor()
  id_servidor = request.args.get("id_servidor", None)
  id_canal = request.args.get("id_canal", None)
  #Url es get_message?id_canal=id&canal_mount=true
  # counts_canal = request.args.get("canal_mount", "false")
  counts = request.args.get("mount", "false")

  if (id_servidor is not None and id_servidor.isdigit()):
    select_sql = "SELECT * FROM Mensajes WHERE id_servidor = %s;"
    cursor.execute(select_sql, (int(id_servidor), ))
    rows = cursor.fetchall()
    result_dicts = [dict(zip(cursor.column_names, row)) for row in rows]
    result_json = json.dumps(result_dicts)
    db.close()
    if counts.lower() == "true":
      dicter = {"count": len(result_dicts)}
      json_re = json.dumps(dicter)
      return json_re
    return result_json
  elif id_canal is not None and id_canal.isdigit():
    select_sql = "SELECT * FROM Mensajes WHERE id_canal = %s;"
    cursor.execute(select_sql, (int(id_canal), ))
    rows = cursor.fetchall()
    result_dicts = [dict(zip(cursor.column_names, row)) for row in rows]
    result_json = json.dumps(result_dicts)
    db.close()
    if counts.lower() == "true":
      dicter = {"count": len(result_dicts)}
      json_re = json.dumps(dicter)
      return json_re
    return result_json
  return "Faile"


@app.route("/", methods=["GET"])
def index():
  return "hola soy index"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
