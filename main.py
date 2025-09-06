from flask import Flask, session, render_template, flash
from config import Config
from forms import TestForm

app = Flask(__name__)
app.config.from_object(Config)

@app.after_request
def set_secure_headers(response):
    response.headers['X-Frame-Options'] = 'Deny'
    response.headers['Content-Security-Policy'] = (
        "default-scr 'self'; "
        "style-src 'self' https://cdn.jsdelivr.net;"
        "script-src 'self' https://cdn.jsdelivr.net;"
    )
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.route("/PP")
def Politica():
    return render_template("PoPri.html")

@app.route("/contact")
def Contactar():
    return render_template("contacto.html")

@app.route("/AskAboutWeb")
def infoDeWeb():
    return render_template("pregunstas.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/test', methods=('GET', 'POST'))
def test():
    form = TestForm()
    #if request.method == 'POST':
    if form.validate_on_submit():
        
        nombre = form.nombre.data.strip()
        apellido = form.apellido.data.strip()
        cumpleaños = form.cumpleaños.data.isoformat()


        with open("datos.txt", "a", encoding="utf-8") as f:
            f.write(f"{nombre}, {apellido}, {cumpleaños}\n")

        return render_template("resultado.html", nombre=nombre, apellido=apellido, cumple=cumpleaños)
    else:
        if form.is_submitted():
            flash("Hubo un problema con el formulario.Verifica los datos", "warning")
    return render_template("formulario.html", form=form)

@app.route("/counter")
def counter():
    count = session.get('count', ) + 1
    session['count'] = count
    return f'Conteo: {count}'

if __name__ == "__main__":
    app.run(debug=False)

