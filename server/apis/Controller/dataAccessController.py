from flask import Blueprint

from service.userService import get_user
from apis.dto.responseDto import user_response_dto, quiz_response_dto, main_response_dto, result_response_dto
from service.quizService import get_quiz
from service.mainService import get_main_result
from service.resultService import get_result

data_api_bp = Blueprint('data_api', __name__, url_prefix='/api')

@data_api_bp.route('/user', methods=['GET'])
def get_users():
  users = get_user()
  return user_response_dto(users)

@data_api_bp.route('/test/test', methods=['GET'])
def get_quiz_contents():
  quizzes = get_quiz()
  return quiz_response_dto(quizzes)

@data_api_bp.route('/', methods=['GET'])
def get_analysis_result():
  result = get_main_result()
  return main_response_dto(result)

@data_api_bp.route('/result/<int:user_id>', methods=['GET'])
def get_users_result(user_id):
  result = get_result(user_id)
  return result_response_dto(result)