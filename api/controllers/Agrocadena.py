from flask import jsonify, request
from db.db import cnx

class Agrocadena():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM agrocadenas")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            # Create a zip object from two lists
            registro = zip(columns, row)
            # Create a dictionary from zip object
            json = dict(registro)
            lista.append(json)
        cur.close
        cnx.close
        return jsonify(lista)

    def create(body):
        # Campos
        data = (body['id'],body['suministro'],body['produccion'],body['distribucion'],body['encargado'])
        # Sentencia SQL
        sql = "INSERT INTO agrocadenas(id, suministro, produccion, distribucion, encargado) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql,data)        
        cnx.commit()
        cur.close
        cnx.close
        return {'estado': "Insertado"}, 200
