from flask import Flask
from .extensions import mongo
from .main import main
from .login import app

def create_app(config_object='flaskmongoprjct.settings'):
	app=Flask(__name__)
	app.config.from_object(config_object)
	mongo.init_app(app)

	app.register_blueprint(login)
	return app