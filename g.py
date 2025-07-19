from flask import Flask, send_file
from requests import post
import random
import string
import time
import threading

# Initialize Flask app
app = Flask(__name__)

# Route to serve b.html at /home
@app.route('/home')
def serve_home():
    return send_file('b.html')

nombres = [
    "Agustin", "Alan", "Alejandro", "Alfonso", "Alonso", "Andres", "Angel", "Antonio", "Ariel", "Armando",
    "Arturo", "Baltazar", "Benjamin", "Boris", "Bruno", "Camilo", "Carlos", "Cesar", "Cristian", "Cristobal",
    "Daniel", "David", "Diego", "Domingo", "Eduardo", "Elias", "Emiliano", "Emilio", "Enrique", "Esteban",
    "Eugenio", "Facundo", "Felipe", "Fernando", "Franco", "Francisco", "Gabriel", "German", "Gonzalo", "Guillermo",
    "Gustavo", "Hector", "Hernan", "Horacio", "Hugo", "Ignacio", "Isaac", "Ismael", "Ivan", "Jaime",
    "Javier", "Jeronimo", "Jesus", "Joaquin", "Jorge", "Jose", "Juan", "Julian", "Julio", "Kevin",
    "Lautaro", "Leonardo", "Lionel", "Lisandro", "Lucas", "Luciano", "Luis", "Manuel", "Marcelo", "Marcos",
    "Mario", "Martin", "Mateo", "Matias", "Maximiliano", "Miguel", "Nicolas", "Octavio", "Omar", "Oscar",
    "Pablo", "Patricio", "Pedro", "Rafael", "Ramiro", "Raul", "Renato", "Ricardo", "Rodrigo", "Roman",
    "Ruben", "Salvador", "Samuel", "Santiago", "Sebastian", "Sergio", "Simon", "Tobias", "Tomas", "Valentin",
    "Vicente", "Victor", "Walter", "Wilfredo", "Xavier", "Yago", "Zacarias", "Abel", "Adrian", "Aldo",
    "Amador", "Anibal", "Arnaldo", "Blas", "Celestino", "Cirilo", "Claudio", "Clemente", "Damian", "Dario",
    "Demetrio", "Dionisio", "Edelmiro", "Efren", "Eliseo", "Esteban", "Ezequiel", "Fabian", "Fausto", "Federico",
    "Flavio", "Gaspar", "Genaro", "Gregorio", "Guido", "Hilario", "Homero", "Ildefonso", "Iker", "Inocencio",
    "Jacinto", "Jacobo", "Jenaro", "Jeremias", "Joaquim", "Jonas", "Jonathan", "Jordan", "Josue", "Justo",
    "Lazaro", "Leandro", "Lorenzo", "Lucio", "Manolo", "Mariano", "Mauricio", "Max", "Melchor", "Moises",
    "Narciso", "Nestor", "Norberto", "Odilio", "Olegario", "Orlando", "Osvaldo", "Pascual", "Perfecto", "Primitivo",
    "Prudencio", "Raimundo", "Reinaldo", "Rene", "Roberto", "Roque", "Rubi", "Rufino", "Sancho", "Segundo",
    "Severo", "Silvestre", "Silverio", "Sixto", "Tadeo", "Teobaldo", "Teodoro", "Timoteo", "Tirso", "Toribio",
    "Tristan", "Ubaldo", "Ulpiano", "Urbano", "Valerio", "Venancio", "Vicenç", "Victoriano", "Vidal", "Waldo",
    "Wenceslao", "Wilmer", "Ximeno", "Yuri", "Zosimo", "Abraham", "Adolfo", "Alfredo", "Bernardo", "Bonifacio"
]


# Lista de apellidos chilenos comunes
apellidos = apellidos = [
    "Gonzalez", "Munoz", "Rojas", "Diaz", "Perez", "Soto", "Contreras", "Silva", "Martinez", "Sepulveda",
    "Morales", "Rodriguez", "Lopez", "Fuentes", "Hernandez", "Torres", "Araya", "Flores", "Espinoza", "Valenzuela",
    "Castillo", "Ramirez", "Reyes", "Gutierrez", "Castro", "Vargas", "Campos", "Alvarez", "Vera", "Lara",
    "Carrasco", "Molina", "Ortiz", "Salazar", "Miranda", "Navarro", "Cortes", "Herrera", "Jara", "Saavedra",
    "Aguilera", "Vega", "Pizarro", "Riquelme", "Cabrera", "Garrido", "Meza", "Bravo", "Tapia", "Olivares",
    "Medina", "Valdes", "Acosta", "Sanchez", "Vidal", "Ponce", "Sandoval", "Alarcon", "Bustamante", "Parra",
    "Aravena", "Mendez", "Chavez", "Cespedes", "Rivas", "Zamora", "Urrutia", "Orellana", "Navarrete", "Villalobos",
    "Figueroa", "Palma", "Paredes", "Vergara", "Delgado", "Quinteros", "Salinas", "Lillo", "Moreno", "Pavez",
    "Venegas", "Maturana", "Gatica", "Cordero", "Cisternas", "Zapata", "Bustos", "Godoy", "Carrillo", "Fuenzalida",
    "Lagos", "Jimenez", "Salgado", "Carmona", "Bravo", "Oliva", "Parraguez", "Rojas", "Yañez", "Lara",
    "Cruz", "Campos", "Acevedo", "Pinto", "Rubio", "Gallardo", "Leiva", "Guzman", "Quiroz", "Jofre",
    "Santana", "Santibanez", "Llanos", "Farias", "Bravo", "Sandoval", "Herrera", "Moraga", "Navarro", "Castro",
    "Garcia", "Lopez", "Diaz", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Ortiz",
    "Gutierrez", "Ramos", "Alvarez", "Jimenez", "Mendoza", "Castillo", "Vargas", "Soto", "Silva", "Leon",
    "Espinoza", "Cortez", "Aguilar", "Molina", "Bravo", "Salinas", "Paredes", "Gonzales", "Alonso", "Moreno",
    "Rojas", "Medina", "Herrera", "Castro", "Cruz", "Ortiz", "Pena", "Campos", "Valencia", "Romero",
    "Vega", "Pizarro", "Carrasco", "Leal", "Navarrete", "Maldonado", "Montes", "Ochoa", "Serrano", "Figueroa",
    "Valdes", "Riquelme", "Palacios", "Sandoval", "Villanueva", "Fuentes", "Bravo", "Guzman", "Lara", "Rojas",
    "Morales", "Carrillo", "Pinto", "Luna", "Vargas", "Herrera", "Flores", "Soto", "Gonzalez", "Diaz",
    "Castillo", "Ramirez", "Ortiz", "Ruiz", "Mendez", "Mora", "Valencia", "Rios", "Rojas", "Paredes"
]


# Generar correo con formato letra+apellido@usm.cl o alumno.usm.cl
def generar_correo_usm():
    letra = random.choice(string.ascii_lowercase)
    apellido = random.choice(apellidos).lower()
    dominio = random.choice(["usm.cl", "alumno.usm.cl", "taisegurowaton.cl","ooohque.weon","tumama.esweona","usm.cl", "alumno.usm.cl","usm.cl", "alumno.usm.cl","usm.cl", "alumno.usm.cl"])

    return f"{letra}{apellido}",f"{dominio}"

def nombre_por_letra(letra, lista_nombres):
    letra = letra.upper()
    candidatos = [nombre.lower() for nombre in lista_nombres if nombre.upper().startswith(letra)]
    if candidatos:
        return random.choice(candidatos)

def generar_correo2(letra):

    dominio = random.choice(["gmail.com", "gmail.com","outlook.com","gmail.com","gmail.com","gmail.com","gmail.com", "gmail.com"])
     
    return random.choice([f"{letra}@{dominio}",f"{letra}{random.randint(1999,2007)}@{dominio}",f"{letra}{random.randint(1999,2007)}@{dominio}", f"{nombre_por_letra(letra[0],nombres)}@{dominio}", f"{nombre_por_letra(letra[0],nombres)}{random.randint(1999,2007)}@{dominio}"])

# Generar string aleatorio
# Cargar la lista de contraseñas rockyou solo una vez, afuera de la función
with open('rockyou.txt', 'r', encoding='latin-1') as f:
    rockyou_passwords = f.read().splitlines()

def generar_texto():
    if random.choice([True, False, True]):
        try:
            with open('rockyou.txt', 'r', encoding='latin-1') as f:
                lines = f.readlines()
                return random.choice(lines).strip()
        except (FileNotFoundError, IndexError):
            k = random.randint(8, 12)
            return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
    else:
        k = random.randint(8, 12)
        return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
        
def gen_AA():
        k = random.randint(25, 30)
        return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
def gen_v():
        k = random.randint(12, 16)
        return ''.join(random.choices(string.digits, k=k))
# Enviar datos falsos
def enviar_datos_falsos(n=10):
    url = "https://usml.weebly.com/ajax/apps/formSubmitAjax.php"  # Corrected form submission URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

    for i in range(n):
        contraseña=generar_texto()
        user=generar_correo_usm()
        datos = {
            "_u371944789852587745": user[0],  # Username
            "_u854971929305915294": f"{user[0]}@{user[1]}",  # Primary email
            "_u209758165131871174": contraseña,  # Password
            "_u946247387613299561": generar_correo2(user[0]),  # Alternate email (non-Gmail)
            "_u997358897365161464": contraseña,  # Second password
            "form_version": "2",
            "wsite_approved": "approved",
            "ucfid": "902981853739546788",
            "recaptcha_token": gen_AA()  # Placeholder: reCAPTCHA token needed
        }

        try:
            # Simulate delay to mimic human behavior
            #time.sleep(random.uniform(1, 3))
            respuesta = requests.post(url, data=datos, headers=headers)
            print(f"[{i+1}] Enviado: {datos['_u946247387613299561'],datos['_u854971929305915294'], datos['_u209758165131871174'],datos['ucfid'],datos['recaptcha_token']} - Estado: {respuesta.status_code}")
            if respuesta.status_code == 200:
                print(f"{respuesta.text}")  # Print first 200 chars of response
            else:
                print(f"Error: Código de estado {respuesta.status_code}")
        except Exception as e:
            print(f"[{i+1}] Error al enviar: {e}")

def run_submission_loop():
    while True:
        enviar_datos_falsos(1000)  # Reduced from 10000 to avoid rate-limiting

if __name__ == "__main__":
    # Start submission loop in a background thread
    submission_thread = threading.Thread(target=run_submission_loop, daemon=True)
    submission_thread.start()
    # Start Flask server
    app.run(host='0.0.0.0', port=5000)

