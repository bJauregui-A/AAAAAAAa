import requests
import os
import subprocess

# URL del archivo rockyou.txt
url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
archivo_destino = "rockyou.txt"

def descargar_archivo(url, destino):
    if not os.path.exists(destino):
        print(f"Descargando {url} ...")
        respuesta = requests.get(url, stream=True)
        if respuesta.status_code == 200:
            with open(destino, 'wb') as f:
                for chunk in respuesta.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Descarga completada.")
        else:
            print(f"Error al descargar: código {respuesta.status_code}")
    else:
        print("Archivo ya existe, omitiendo descarga.")

def ejecutar_script(script):
    print(f"Ejecutando {script} ...")
    subprocess.run(["python", script])

if __name__ == "__main__":
    descargar_archivo(url, archivo_destino)
    ejecutar_script("g.py")
