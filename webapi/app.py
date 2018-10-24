from flask import Flask # http://flask.pocoo.org/docs/1.0/quickstart/#quickstart
from flask import request
from flask import jsonify

from flask_restful import Resource, Api, reqparse # https://flask-restful.readthedocs.io/en/latest/
from flask_swagger import swagger # https://github.com/gangverk/flask-swagger
from flask_swagger_ui import get_swaggerui_blueprint # https://pypi.org/project/flask-swagger-ui/


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

# Swagger  setup and configuration
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


class HelloWorld(Resource):
    def get(self):
        # swagger_from_file: /hello.yml

        '''
        Get a hello message
        ---
        responses:
          200:
            description: Message returned
        '''
        return {'message': 'Hello space!'}


class PredictionModel(Resource):
    def get(self):
        # swagger_from_file: /prediction.yml
        # 
        '''
        Just ping
        ---
        responses:
          200:
            description: Ok message
        '''
        return {'message': "I'm alive!"} 

    def post(self):       
        '''
        Get a prediction/forecast of energy consumption based on consumption data and weather data
        ---
        parameters:
          - in: body
        responses:
          200:
            description: Prediction result(s)
          400:
            description: Request was broken (propably the request payload)
        '''
        # https://stackoverflow.com/questions/11817182/uploading-multiple-files-with-flask
        uploaded_files = request.files.getlist("files")
        print(uploaded_files)

        return {'message': 'Here will be a electricity consumption forecast. '}         


# activate paths
api.add_resource(HelloWorld, '/hello')
api.add_resource(PredictionModel, '/predict')


# swagger spec generator
@app.route("/specs")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "0.1b"
    swag['info']['title'] = "Data Science Electricity Project API"
    return jsonify(swag)


if __name__ == '__main__':
    app.run(debug=True)
