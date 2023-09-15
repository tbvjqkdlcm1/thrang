from db_connect import db

class Result(db.Model):
  
  __tablename__ = 'result'
  
  id             = db.Column(db.Integer, primary_key=True, nullable=False)
  user_id        = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
  quiz_score     = db.Column(db.Integer, nullable=False)
  ox_list        = db.Column(db.String(256), nullable=False, server_default='OOOXXXOOXX')
  exam_time      = db.Column(db.Integer, nullable=False)
  delivery_count = db.Column(db.Integer, nullable=False)
  
  def __init__(self, user_id, quiz_score, ox_list, exam_time, delivery_count):
    self.user_id        = user_id
    self.quiz_score     = quiz_score
    self.ox_list        = ox_list
    self.exam_time      = exam_time
    self.delivery_count = delivery_count