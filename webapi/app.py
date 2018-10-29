from flask import Flask # http://flask.pocoo.org/docs/1.0/quickstart/#quickstart
from flask import jsonify, render_template

from flask_restful import Api # https://flask-restful.readthedocs.io/en/latest/
from flask_swagger import swagger # https://github.com/gangverk/flask-swagger
from flask_swagger_ui import get_swaggerui_blueprint # https://pypi.org/project/flask-swagger-ui/
from flask_cors import CORS # https://flask-cors.readthedocs.io/en/latest/

from src.resources import HelloSpace, PredictionModelIndustry, PredictionModelCommercialBuilding, PredictionModelApartmentBuilding


app = Flask(__name__)
api = Api(app)
CORS(app)


# activate/register paths
api.add_resource(HelloSpace, '/hello')
api.add_resource(PredictionModelIndustry, '/predict/industry')
api.add_resource(PredictionModelCommercialBuilding, '/predict/commercial-building')
api.add_resource(PredictionModelApartmentBuilding, '/predict/apartment-building')


# API documentation setup and configuration
SWAGGER_URL = '/api/specs'
API_URL = '/specs'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, # Swagger UI path
    API_URL,
    config={ # Swagger UI config overrides
        'app_name': "Test application"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# index html
@app.route("/")
def root():
    return render_template("index.html")


# API documentation spec generator
@app.route("/specs")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "0.1b"
    swag['info']['title'] = "Data Science Electricity Project API"
    return jsonify(swag)


if __name__ == '__main__':
    app.run(debug=True)
