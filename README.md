# prex-challenge

Este proyecto incluye un agente desarrollado en GO que recolecta información del sistema operativo de servidores Linux y Windows. Además una API en Flask que recibe y almacena esta información en archivos CSV permitiendo su consulta a trevés de endpoints.

## Dependencias

### Agente (Go)

- **Go 1.16** o superior.

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

1. Instala Go en tu sistema desde [golang.org](https://golang.org).
2. Clona este repositorio:
   ```bash
   git clone https://github.com/longojp/prex-challenge.git
   cd prex-challenge


go build -o agent.exe agent.go

GOOS=linux GOARCH=amd64 go build -o agent-linux agent.go

.\agent.exe

./agent-linux


### API (Python)

1. Instala Python 3.x en tu sistema.
2. Instala las dependencias necesarias usando el archivo `requirements.txt`:
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


   






