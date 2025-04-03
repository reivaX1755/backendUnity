from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS  # Importamos CORS para habilitar el acceso desde diferentes orígenes
from config import Config
import datetime

app = Flask(__name__)
app.config.from_object(Config)

# Habilitamos CORS para permitir solicitudes de cualquier origen
CORS(app)

mysql = MySQL(app)

@app.route('/test_db')
def test_db():
    try:
        cursor = mysql.connection.cursor()
        # Usamos el nuevo nombre de base de datos
        cursor.execute("USE bdplataformas2d_connect")
        cursor.execute("SELECT DATABASE()") 
        db_name = cursor.fetchone()
        cursor.close()
        return f"Conectado a la base de datos: {db_name}"
    except Exception as e:
        return f"Error al conectar a la base de datos: {str(e)}"

@app.route('/topPartidas', methods=['GET'])
def get_top_partidas():
    try:
        cursor = mysql.connection.cursor()
        # Usamos el nuevo nombre de base de datos
        cursor.execute("USE bdplataformas2d_connect")
        cursor.execute("SELECT id, monedas, fecha_hora FROM partidas ORDER BY monedas DESC LIMIT 8")
        partidas = cursor.fetchall()
        cursor.close()
        
        partidas_list = [
            {
                'id': partida[0],
                'monedas': partida[1],
                'fecha_hora': partida[2].strftime('%Y-%m-%d %H:%M:%S') if partida[2] else None
            }
            for partida in partidas
        ]
        
        return jsonify(partidas_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/partidas', methods=['POST'])
def add_partida():
    try:
        data = request.get_json()
        monedas = data['monedas']
        fecha_hora = datetime.datetime.now()
        
        cursor = mysql.connection.cursor()
        # Usamos el nuevo nombre de base de datos
        cursor.execute("USE bdplataformas2d_connect")
        cursor.execute(
            "INSERT INTO partidas (monedas, fecha_hora) VALUES (%s, %s)",
            (monedas, fecha_hora)
        )
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'message': 'Partida añadida correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == "__main__":
    app.run()
