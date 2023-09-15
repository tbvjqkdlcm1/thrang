from db_connect import db

class Recycling(db.Model):

  __tablename__ = 'recycling'

  id    = db.Column(db.Integer, primary_key=True, nullable=False)
  title = db.Column(db.NVARCHAR(256), nullable=False)
  image = db.Column(db.Text, nullable=False)

  def __init__(self, title, image):
    self.title = title
    self.image = image