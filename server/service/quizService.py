from domain.dao.quizDao import all_quiz
from domain.dao.exampleDao import all_examples

def get_quiz():
  quiz_data = all_quiz()
  result = []
  for quiz in quiz_data:

    example_list = all_examples(quiz.id)
    examples = []
    total_count = 0
    correct_count = 0
    for example in example_list:
      examples.append(example.content)
      total_count += example.count
      if quiz.answer == example.num:
        correct_count = example.count
    
    ratio = (correct_count / total_count) * 100
    result.append({
        "question": quiz.question,
        "examples": examples,
        "ratio": ratio
    })
  return result