# Proyecto Flask Python IPLACEX

Este proyecto es una aplicación web desarrollada con Flask que incluye dos ejercicios principales:

## Ejercicio 1: Cálculo de Compras de Pintura
- Calcula el precio total de tarros de pintura
- Aplica descuentos según la edad del cliente:
  - 15% para personas entre 18 y 30 años
  - 25% para personas mayores de 30 años
  - Sin descuento para menores de 18 años
- Precio base por tarro: $9000

## Ejercicio 2: Sistema de Login
- Sistema de autenticación con dos tipos de usuarios:
  - Administrador (usuario: juan, contraseña: admin)
  - Usuario normal (usuario: pepe, contraseña: user)
- Panel de control personalizado según el rol del usuario

## Características
- Interfaz responsiva y amigable
- Validación de formularios
- Manejo de sesiones de usuario
- Protección de rutas mediante decoradores
- Estilos CSS personalizados

## Tecnologías Utilizadas
- Python
- Flask
- HTML
- CSS
- JavaScript

## Estructura del Proyecto 

## Instrucciones de Inicio

1. Clonar el repositorio:
```bash
git clone https://github.com/Eduvinte/flaskpythoniplacex.git
cd flaskpythoniplacex
```

2. Crear y activar entorno virtual (opcional pero recomendado):
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install flask
```

4. Ejecutar la aplicación:
```bash
python app.py
```

5. Abrir en el navegador:
```
http://127.0.0.1:5000
```

### Credenciales de prueba:
- Administrador:
  - Usuario: juan
  - Contraseña: admin

- Usuario normal:
  - Usuario: pepe
  - Contraseña: user

Repo: https://github.com/Eduvinte/flaskpythoniplacex