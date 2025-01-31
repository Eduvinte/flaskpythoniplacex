from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para manejar sesiones

# Datos de usuarios para el ejercicio 2
USERS = {
    "juan": {"password": "admin", "role": "administrador"},
    "pepe": {"password": "user", "role": "usuario"}
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('ejercicio2'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
@login_required
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        cantidad = int(request.form.get('cantidad'))
        
        # Cálculo del precio base
        precio_base = cantidad * 9000
        
        # Cálculo del descuento según la edad
        descuento = 0
        if 18 <= edad <= 30:
            descuento = precio_base * 0.15
        elif edad > 30:
            descuento = precio_base * 0.25
            
        total = precio_base - descuento
        
        return render_template('ejercicio1.html', 
                             nombre=nombre,
                             total_sin_descuento=precio_base,
                             descuento=descuento,
                             total=total,
                             mostrar_resultados=True)
    
    return render_template('ejercicio1.html', mostrar_resultados=False)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form.get('nombre')
        password = request.form.get('password')
        
        if username in USERS and USERS[username]["password"] == password:
            mensaje = f"Bienvenido {USERS[username]['role']} {username}"
            session['usuario'] = username  # Guardamos el usuario en la sesión
            return render_template('dashboard.html', mensaje=mensaje)
        else:
            mensaje = "Usuario o contraseña incorrectos"
            return render_template('ejercicio2.html', mensaje=mensaje)
            
    return render_template('ejercicio2.html', mensaje="")

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)