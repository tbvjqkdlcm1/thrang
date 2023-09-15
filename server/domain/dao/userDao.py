from domain.models.user import User

def all_user():
  result = User.query.order_by(User.id.desc()).all()
  return result