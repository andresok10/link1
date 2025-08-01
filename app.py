from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta,date,datetime
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto por una clave secreta segura
app.permanent_session_lifetime = timedelta(days=31)

# URLs iniciales
links = {
    "YouTube": "https://www.youtube.com/",
    "OneDrive": "https://librefutbol.su/eventos/?r=aHR0cHM6Ly9jYW5kbGVyLmJlYXV0eS92b2QuaHRtbD9nZXQ9aHR0cHM6Ly92b29kYy5jb20vZW1iZWQvODU4YTkzOTBhMTg0OGE5Mzg3OTk4MzhiOTU4Yjk4ODU4Yjk2Lmh0bWw=",
    "ecuabet": "https://ecuabet.com/deportes/partido/10613354?utm_source=Directa&utm_medium=Invasivo&utm_campaign=Evento_Tactico_ECU_Oct2024&utm_term=Evento&utm_content=Evento_Tactico_ECU_Oct2024",
    "mega": "https://www.bilibili.tv/en/video/2042945247",
    "mega2": "https://getbootstrap.com/docs/5.0/getting-started/introduction/",
    "mega3": "https://reclutamiento.tia.com.ec/buscar",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    # Obtenemos las URLs guardadas en la sesión y las combinamos con las URLs iniciales
    saved_links = session.get('saved_links', {})
    combined_links = {**links, **saved_links}
    
    # Obtener datos del formulario para agregar una nueva URL
    name = request.form.get('name')
    url = request.form.get('url')
    
    if name and url:
        # Guardar la nueva URL en la sesión
        saved_links[name] = url
        session['saved_links'] = saved_links
        return redirect(url_for('index'))
    
    return render_template('index.html', links=combined_links)

# Ruta para eliminar una URL guardada en la sesión
@app.route('/delete/<string:name>', methods=['POST'])
def delete_url(name):
    saved_links = session.get('saved_links', {})
    if name in saved_links:
        del saved_links[name]
        session['saved_links'] = saved_links
    return redirect(url_for('index'))

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(host='0.0.0.0', debug=True)