from flask import Flask,render_template
app = Flask(__name__)

# Rutas
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/proyectos")
def ruta():
    return render_template("proyectos.html")
#Iniciar app
def run_app():
    return app.run(debug=True)

if __name__ == "__main__":
    run_app()
