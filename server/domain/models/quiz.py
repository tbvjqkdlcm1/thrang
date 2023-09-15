from db_connect import db

class Quiz(db.Model):

  __tablename__ = 'quiz'

  id        = db.Column(db.Integer, primary_key=True, nullable=False)
  question  = db.Column(db.NVARCHAR(256), nullable=False)
  quiz_type = db.Column(db.Integer, nullable=False)
  answer    = db.Column(db.Integer, nullable=False)

  def __init__(self, question, quiz_type, answer):
    self.question = question
    self.quiz_type = quiz_type
    self.answer = answer