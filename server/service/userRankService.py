from domain.dao.resultDao import all_result, user_result

def get_user_rank(user_id):
  user_result_data = user_result(user_id)
  if user_result_data == None:
    return None
  
  all_result_data = all_result()
  
  user_quiz_score = user_result_data.quiz_score * 10
  user_exam_time = user_result_data.exam_time
  user_delivery_count = user_result_data.delivery_count
  user_final_score = user_quiz_score + (1/user_exam_time) - 3*user_delivery_count*(user_delivery_count+1)/2
  
  rank = 1
  for result in all_result_data:
    temp_quiz_score = result.quiz_score * 10
    temp_exam_time = result.exam_time
    temp_delivery_count = result.delivery_count
    temp_final_score = temp_quiz_score + (1/temp_exam_time) - 3*temp_delivery_count*(temp_delivery_count+1)/2
    
    if temp_final_score < user_final_score:
      rank += 1
    
  return rank