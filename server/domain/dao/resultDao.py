from domain.models.result import Result, db

def new_result(userid, score, oxlist, examtime, deliverycount):
  result = Result(user_id = userid, quiz_score = score, ox_list=oxlist, exam_time = examtime, delivery_count = deliverycount)
  db.session.add(result)
  db.session.commit()
  return result

def all_result():
  result = Result.query.order_by(Result.id.desc()).all()
  return result

def user_result(user_id):
  result = Result.query.filter_by(user_id=user_id).first()
  return result