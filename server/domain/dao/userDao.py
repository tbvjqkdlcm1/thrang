from domain.models.user import User

def all_user():
  result = User.query.order_by(User.id.desc()).all()
  return result

def one_user(user_id):
  result = User.query.filter_by(id=user_id).first()
  return result