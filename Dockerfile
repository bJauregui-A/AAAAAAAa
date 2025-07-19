# Usa una imagen oficial de Python
# Imagen base con Python
FROM python:3.11-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar tus scripts al contenedor
COPY b.py .
COPY g.py .

# Instalar requests
RUN pip install requests

# Ejecutar el script principal
CMD ["python", "b.py"]
