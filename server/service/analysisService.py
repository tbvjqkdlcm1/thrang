from domain.dao.userDao import new_user
from domain.dao.resultDao import new_result
from domain.dao.quizDao import all_quiz
from domain.dao.exampleDao import count_example

def analysis_service(result):
  #new 유저
  user = new_user(result['user_name'])
  score, ox_list = score_service(result['answers'])
  
  start_time = result['start_time']
  end_time = result['end_time']
  delivery_count = result['delivery_count']
  
  exam_time = end_time - start_time
  
  new_result(userid=user.id, score=score, oxlist=ox_list,  examtime=exam_time, deliverycount=delivery_count)

  return user.id

def score_service(answers):
  quizzes = all_quiz()
  ox_list = ['X' for _ in range(10)]
  ox_list_idx = 0
  score = 0
  for quiz, answer in zip(quizzes, answers):
    if quiz.answer == answer:
      score += 1
      ox_list[ox_list_idx] = 'O'
    ox_list_idx += 1
      
    count_example(quiz.id, answer)
  
  ox_list = ''.join(ox_list)
  return score, ox_list