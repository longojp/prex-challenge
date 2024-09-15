import os
import csv
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Guardan archivos csv
csv_directory = '/var/log/prex_log'

# Recibir los datos y guardarlos en un archivo csv
@app.route('/collect', methods=['POST'])
def collect_data():
    data = request.get_json()

    ip_address = request.remote_addr  # Obtener IP que envía solicitud
    date_str = datetime.now().strftime('%Y-%m-%d')  # Fecha actual
    csv_filename = f"{ip_address}_{date_str}.csv"
    csv_path = os.path.join(csv_directory, csv_filename)

    # Crear el directorio si no existe
    os.makedirs(csv_directory, exist_ok=True)

    # Guardar los datos en un archivo csv
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Informacion sobre el procesador'])
        writer.writerow([data.get('cpu_info')])
        writer.writerow(['Listado de procesos'])
        writer.writerows([[process] for process in data.get('processes', [])])
        writer.writerow(['Usuarios con sesion abierta'])
        writer.writerows([[user] for user in data.get('users', [])])
        writer.writerow(['Nombre del sistema operativo'])
        writer.writerow([data.get('os_name')])
        writer.writerow(['Version del sistema operativo'])
        writer.writerow([data.get('os_version')])

    return jsonify({"status": "Data received and saved!"}), 200

# Consulta de la información por IP
@app.route('/query', methods=['GET'])
def query_data():
    ip_address = request.args.get('ip')
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    csv_filename = f"{ip_address}_{date_str}.csv"
    csv_path = os.path.join(csv_directory, csv_filename)

    # Verificar si el archivo existe
    if not os.path.exists(csv_path):
        return jsonify({"error": "No se encontraron datos para esta IP y fecha"}), 404

    # Leer el contenido del archivo csv
    with open(csv_path, mode='r') as file:
        csv_content = file.read()

    return jsonify({"status": "Success", "data": csv_content}), 200

if __name__ == '__main__':
    # Cert y clave en /home/ubuntu/
    app.run(host='0.0.0.0', port=8080, ssl_context=('/home/ubuntu/cert.pem', '/home/ubuntu/key.pem'))