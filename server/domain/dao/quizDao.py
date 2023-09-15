from domain.models.quiz import Quiz

def all_quiz():
  result = Quiz.query.order_by(Quiz.id.asc()).all()
  return result
