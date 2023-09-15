from db_connect import db

class Article(db.Model):

  __tablename__ = 'article'

  id    = db.Column(db.Integer, primary_key=True, nullable=False)
  title = db.Column(db.NVARCHAR(256), nullable=False)
  image = db.Column(db.Text, nullable=False)
  url   = db.Column(db.Text, nullable=False)

  def __init__(self, title, image, url):
    self.title = title
    self.image = image
    self.url   = url