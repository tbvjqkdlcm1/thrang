from flask.json import jsonify

def user_response_dto(user):
  return jsonify(user),200

def quiz_response_dto(quiz):
  return jsonify(quiz), 200

def main_response_dto(result):
  return jsonify(result), 200 

def result_response_dto(result):
  if result == 'Not Found User':
    return jsonify(result), 400
  return jsonify(result), 200

def user_ranking_response_dto(ranks):
  if ranks == 'Not Found User':
    return jsonify(ranks), 400
  return jsonify(ranks), 200