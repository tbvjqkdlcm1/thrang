from flask.json import jsonify

def user_response_dto(user):
  print("wow")
  return jsonify(user),200