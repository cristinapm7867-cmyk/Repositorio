from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

if __name__ == '__main__':
    app.run(debug=True)