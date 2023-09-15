from flask import Flask
from flask_migrate import Migrate
import logging

from apis.Controller.dataAccessController import data_api_bp

from db_connect import db
import config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(data_api_bp)
    app.config.from_object(config)

    db.init_app(app)
  
    migrate = Migrate()
    migrate.init_app(app, db, compare_type=True)

    @app.route('/cc')
    def start():
        return "chicken~~~"

    return app

# 로깅 설정
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("This is log's info")
logging.warning("This is warning logging message")

if __name__ == "__main__":
  create_app().run('0.0.0.0', port=80, debug=True)