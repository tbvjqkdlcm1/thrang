from flask.json import jsonify

def user_response_dto(user):
  return jsonify(user),200

def quiz_response_dto(quiz):
  return jsonify(quiz), 200

def main_response_dto(result):
  return jsonify(result), 200 