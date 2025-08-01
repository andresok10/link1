from flask import Flask, render_template, request, redirect, url_for,session
from datetime import timedelta,date,datetime
app = Flask(__name__)
app.secret_key = 'supersecretkey'
#app.permanent_session_lifetime = timedelta(days=31) solo sirve con session.get()
default_links = {
    "YouTube": "https://www.youtube.com/",
    "OneDrive": "https://librefutbol.su/eventos/?r=aHR0cHM6Ly9jYW5kbGVyLmJlYXV0eS92b2QuaHRtbD9nZXQ9aHR0cHM6Ly92b29kYy5jb20vZW1iZWQvODU4YTkzOTBhMTg0OGE5Mzg3OTk4MzhiOTU4Yjk4ODU4Yjk2Lmh0bWw=",
    "ecuabet": "https://ecuabet.com/deportes/partido/10613354?utm_source=Directa&utm_medium=Invasivo&utm_campaign=Evento_Tactico_ECU_Oct2024&utm_term=Evento&utm_content=Evento_Tactico_ECU_Oct2024",
    "mega": "https://www.bilibili.tv/en/video/2042945247",
    "mega2": "https://getbootstrap.com/docs/5.0/getting-started/introduction/",
    "mega3": "https://reclutamiento.tia.com.ec/buscar",
}
# Lista global para guardar nuevos links
saved_links = {}

@app.route("/", methods=["GET", "POST"])
def index():
    #session.permanent = True  # <- esto activa los 31 días
    global saved_links  # usar la lista global
    if request.method == "POST": # Obtener datos del formulario para agregar una nueva URL
        name = request.form.get("name")
        url = request.form.get("url")
        if name and url:
            saved_links[name] = url # Guardar la nueva URL en la sesión
            return redirect(url_for("index"))
    combined_links = {**default_links, **saved_links}
    return render_template("index.html", links=combined_links)

@app.route("/delete/<string:name>", methods=["POST"])
def delete(name):
    global saved_links
    saved_links.pop(name, None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=2000, debug=True)
    #app.run(host='0.0.0.0', debug=True) # python app.py