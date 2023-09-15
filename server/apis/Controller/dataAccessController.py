from flask import Blueprint

from service.userService import get_user
from apis.dto.responseDto import user_response_dto, quiz_response_dto
from service.quizService import get_quiz

data_api_bp = Blueprint('data_api', __name__, url_prefix='/api')

@data_api_bp.route('/user', methods=['GET'])
def get_users():
  users = get_user()
  return user_response_dto(users)

@data_api_bp.route('/test/test', methods=['GET'])
def get_quiz_contents():
  quizzes = get_quiz()
  return quiz_response_dto(quizzes)