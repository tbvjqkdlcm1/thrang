from domain.models.article import Article

def all_article():
  result = Article.query.all()
  return result