# Usa una imagen oficial de Python
FROM python:3.12-slim

# Copia tu código al contenedor
COPY b.py .

# Comando por defecto para ejecutar tu archivo Python
CMD ["python", "b.py"]
