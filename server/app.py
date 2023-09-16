from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
import logging

from apis.Controller.dataAccessController import data_api_bp
from apis.Controller.analysisController import analysis_bp

from db_connect import db
import config
import json

def create_app():
    app = Flask(__name__)
    app.register_blueprint(data_api_bp)
    app.register_blueprint(analysis_bp)
    app.config.from_object(config)

    db.init_app(app)
  
    migrate = Migrate()
    migrate.init_app(app, db, compare_type=True)

    CORS(app, resources={r'*':{'origins':'*'}}, supports_credentials=True)

    return app

# 로깅 설정
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 로그 데이터를 JSON 파일에 추가
log_data = {
    'message': '한글로 된 로그 데이터',
    'value': 42
}

# 로그 데이터를 JSON 문자열로 변환
log_json = json.dumps(log_data, ensure_ascii=False)

# JSON 파일에 로그 데이터 추가
logger.info(log_json)

# 로그 파일 닫기
logging.shutdown()


if __name__ == "__main__":
  create_app().run('0.0.0.0', port=80, debug=True)