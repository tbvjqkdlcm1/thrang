from domain.models.user import User, db
from domain.models.result import Result

def all_user():
  result = User.query.order_by(User.id.desc()).all()
  return result

def one_user(user_id):
  result = User.query.filter_by(id=user_id).first()
  return result

def new_user(name):
  user = User(name)
  db.session.add(user)
  db.session.commit()
  return user

def all_user_result():
  result = User.query.join(Result, User.id == Result.user_id).add_columns(User.name, Result.user_id, Result.quiz_score, Result.ox_list, Result.exam_time, Result.delivery_count).all()
  return result