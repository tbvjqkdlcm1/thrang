from flask import Blueprint

from service.userService import get_user
from apis.dto.responseDto import user_response_dto

data_api_bp = Blueprint('data_api', __name__, url_prefix='/api')

@data_api_bp.route('/user', methods=['GET'])
def get_users():
  users = get_user()
  print("hambuuuuuuuk")
  return user_response_dto(users)