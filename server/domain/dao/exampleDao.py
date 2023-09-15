from domain.models.example import Example, db

def all_examples(quiz_id):
  example_list = Example.query.filter_by(quiz_id=quiz_id).all()
  return example_list

def count_example(quiz_id, num):
  example = Example.query.filter_by(quiz_id=quiz_id, num=num).first()
  example.count += 1
  db.session.commit()
  pass