
-------------------------------------------------------------------------------

Http API for electricity consumption prediction service

https://ds-2018-webapi.herokuapp.com/

Tiny Flask server application to serve electricity consumption prediction API.
Uses C3.js chart library in graphs (https://c3js.org/).



* Module dependencies
-------------------------------------------------------------------------------
flask            http://flask.pocoo.org/docs/1.0/quickstart/#quickstart
flask_restful    https://flask-restful.readthedocs.io/en/latest/
flask_swagger    https://github.com/gangverk/flask-swagger
flask_swagger_ui https://pypi.org/project/flask-swagger-ui/
Flask-CORS       https://flask-cors.readthedocs.io/en/latest/
pandas           https://pandas.pydata.org/pandas-docs/stable/index.html
statsmodels      https://www.statsmodels.org/stable/index.html
scipy            https://www.scipy.org/
sklearn          https://scikit-learn.org/stable/


* Setup
-------------------------------------------------------------------------------
pip install flask
pip install flask_restful
pip install flask_swagger
pip install flask_swagger_ui
pip install flask-cors
pip install pandas
pip install -U statsmodels
pip install scipy
pip install sklearn


* Running without Docker
-------------------------------------------------------------------------------
In terminal go to webapi folder and execute "flask run"
Local dev server starts in address http://127.0.0.1:5000/ 


* Running with Docker
-------------------------------------------------------------------------------
In terminal go to webapi folder (location of the Dockerfile)
build image: "docker build -t flask-api ."
run image:   "docker run -p 5000:5000 flask-api"
Container starts and serves the api in address http://127.0.0.1:5000


* API Documentation
-------------------------------------------------------------------------------
API documentation available in Swagger format: 
https://ds-2018-webapi.herokuapp.com/api/specs/

