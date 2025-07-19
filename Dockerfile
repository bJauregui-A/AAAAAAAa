# Imagen base ligera
FROM python:3.12-slim

# Establece directorio de trabajo
WORKDIR /app

# Instala wget (muy liviano)
# Descarga directa del diccionario rockyou.txt
RUN apt update && apt install -y wget
RUN wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
RUN pip install requests --no-cache-dir requests python-anticaptcha
# Copia tu script Python
COPY g.py .

# Comando de inicio
CMD ["python", "g.py"]
