from db_connect import db

class Example(db.Model):

  __tablename__ = 'example'

  id         = db.Column(db.Integer, primary_key=True, nullable=False)
  quiz_id    = db.Column(db.Integer, db.ForeignKey('quiz.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
  content    = db.Column(db.NVARCHAR(256), nullable=False)
  num        = db.Column(db.Integer, nullable=False)
  count      = db.Column(db.Integer, nullable=False, default=0)

  def __init__(self, content, quiz_id, num):
    self.content = content
    self.quiz_id = quiz_id
    self.num     = num