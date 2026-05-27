from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

# Diccionario para guardar los enlaces en la memoria del programa
# Formato: {"codigo_corto": "url_larga_original"}
url_db = {}

def generar_codigo():
    # Genera 5 letras/números aleatorios para el enlace corto
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(5))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url_larga = request.form["url_larga"]
        codigo = generar_codigo()
        url_db[codigo] = url_larga  # Guardamos en nuestro "diccionario-base de datos"
        
        # Creamos el enlace corto local
        enlace_corto = f"http://localhost:5000/{codigo}"
        return render_template("resultado.html", enlace_corto=enlace_corto)
    
    return render_template("index.html")

@app.route("/<codigo>")
def redireccionar(codigo):
    # Si el código existe en nuestra memoria, redirige a la URL original
    url_original = url_db.get(codigo)
    if url_original:
        return redirect(url_original)
    return "<h1>Error: El enlace no existe</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)

    