# prex-challenge

Este proyecto incluye un agente desarrollado en GO que recolecta información del sistema operativo de servidores Linux y Windows. Además una API en Flask que recibe y almacena esta información en archivos CSV permitiendo su consulta a trevés de endpoints.

## Dependencias

### Agente (Go)

- **Go 1.23** o superior.

### API (Python)

- Flask 3.0.3
- Python 3.x

## Estructura del Proyecto

- `agent-linux`: Código del agente en Go que recolecta información del sistema operativo Linux.
- `agent.exe`: Código del agente en Go que recolecta información del sistema operativo Windows.
- `app.py`: Código de la API en Python que recibe y almacena la información.
- `requirements.txt`: Archivo que contiene las dependencias necesarias para ejecutar la API.
- `agent.go`: Archivo con código de agente para Linux y Windows.

## Instalación

### Agente (Go)

1. Instalar Go en tu sistema desde [golang.org](https://golang.org).
2. Clonar este repositorio:
   ```bash
   git clone https://github.com/longojp/prex-challenge.git
   cd prex-challenge


go build -o agent.exe agent.go

GOOS=linux GOARCH=amd64 go build -o agent-linux agent.go

.\agent.exe

./agent-linux


### API (Python)

1. Instalar Python 3.x en tu sistema.
2. Instalar las dependencias necesarias usando el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt

   python app.py

### Uso
Ejecutar Agente

1. En Windows
   .\agent.exe
2. En Linux
   cu./agent-linux


### Consultar  API

1. Para consultar por IP
   curl -k "https://<IP>:8080/query?ip=xx.xx.xx.xx"
2. Para consultar por IP y fecha
   curl -k "https://<IP>:8080/query?ip=xx.xx.xx.xx&date=2024-09-15"

## Código Fuente del Agente

El código fuente del agente está disponible en el archivo [`agent.go`](./agent.go) para su revisión. Este código fue desarrollado en **Go** y es responsable de recolectar la información del sistema operativo y enviarla a la API.

## Código Fuente de la API

El código fuente de la API está disponible en el archivo [`app.py`](./app.py). Esta API fue desarrollada en **Python** usando **Flask** y es responsable de recibir, almacenar y permitir la consulta de los datos enviados por el agente.
   

## Instancias

1. prex-win - Servidor Windows 2022 donde se ejecuta agent.exe

2. prex-api - Servidor Linux Ubuntu donde se ejecuta API

3. prex-linux - Servidor Linux Ubuntu donde se ejecuta agent-linux

## Evidencia de ejecución en AWS EC2

A continuación se muestra una captura de las instancias **Windows** y **Linux** corriendo en AWS EC2:

![Evidencia de instancias EC2 corriendo]



![image](https://github.com/user-attachments/assets/fd953f71-652a-4b96-ae82-0a59cc87ae03)


Detalles prex-win

![image](https://github.com/user-attachments/assets/e0e19e90-1e29-479f-a61d-44cac7130d38)


Dealles prex-api

![image](https://github.com/user-attachments/assets/faffccc0-3049-4954-9893-e50a740e2b61)

Detalles prex-linux

![image](https://github.com/user-attachments/assets/e6d03d41-5d50-494d-9fa8-8ce256fa8682)


## Evidencia de la API corriendo directamente en la instancia API

![image](https://github.com/user-attachments/assets/0b4e4e27-b34f-4da8-8912-5ca4de8b0d46)

## Evidencia de los archivos CSV generados por la API

![image](https://github.com/user-attachments/assets/9355752f-15eb-4b83-b881-ebc75d3df59d)

## Evidencia de Solicitud CURL a la API desde Instancia API

![image](https://github.com/user-attachments/assets/f11e44f9-dff7-4d96-a7f3-9c6281b20a0a)




