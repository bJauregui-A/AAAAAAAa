# Imagen base ligera
FROM python:3.12-slim

# Establece directorio de trabajo
WORKDIR /app

# Instala wget (muy liviano)
RUN apt update && apt install -y wget --no-install-recommends && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Descarga directa del diccionario rockyou.txt
RUN wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

# Copia tu script Python
COPY g.py .

# Comando de inicio
CMD ["python", "g.py"]
