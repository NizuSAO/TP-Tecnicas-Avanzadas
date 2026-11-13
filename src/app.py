
from flask import Flask

# Importamos nuestros controladores
from controllers.categoria_controller import categorias_bp
from controllers.productos_controller import productos_bp

# Creamos nuestra aplicación Flask
app = Flask(__name__)

# Registramos los controladores
app.register_blueprint(categorias_bp)
app.register_blueprint(productos_bp)

# Iniciamos el servidor
if __name__ == "__main__":
    app.run(debug=True)
