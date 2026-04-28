from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

#Importar Blueprints (los creadores en las próximas features)
from routes.products import products_bp
from routes.cart import cart_bp


def create_app():

    app = Flask(__name__)

    #Habilitar CORS (necesario para Etapa 2 con frontend)
    CORS(app)

    #Configurar Swagger 
    app.config['SWAGGER'] = {
        'title': 'Coffee Cart API',
        'uiversion': 3
    }
    Swagger(app)

    #Registrar blueprints
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(cart_bp, url_prefix='/cart')


    return app


    # Punto de entrada
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)