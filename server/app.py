from flask import Flask, render_template
from flask_migrate import Migrate
from flask_cors import CORS

from apis.Controller.dataAccessController import data_api_bp
from apis.Controller.analysisController import analysis_bp

from db_connect import db
import config

from log import JsonFormatter

def create_app():
    app = Flask(__name__)
    app.register_blueprint(data_api_bp)
    app.register_blueprint(analysis_bp)
    app.config.from_object(config)

    db.init_app(app)
  
    migrate = Migrate()
    migrate.init_app(app, db, compare_type=True)

    CORS(app, resources={r'*':{'origins':'http://trashsupply.net'}}, supports_credentials=True)

    @app.route('/')
    def health_check():
        return render_template('index.html')

    return app

if __name__ == "__main__":
  create_app().run('0.0.0.0', port=80, debug=True)