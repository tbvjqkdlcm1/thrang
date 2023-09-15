import random

from domain.dao.resultDao import user_result, all_result
from domain.dao.userDao import one_user
from domain.dao.articleDao import all_article
from domain.dao.recyclingDao import all_recycling

from .userRankService import get_user_rank


def get_result(user_id):
  result_data = user_result(user_id)
  user_data = one_user(user_id)
  ranking = get_user_rank(user_id)
  
  if result_data == None or user_data == None or ranking == None:
    return "Not Found User"
  
  delivery_count = result_data.delivery_count
  quiz_score = result_data.quiz_score
  final_score = quiz_score*10 - 3*delivery_count*(delivery_count+1)/2
  user_name = user_data.name
  tier_url = {1: '/images/grade_1.png',
              2: '/images/grade_2.png',
              3: '/images/grade_3.png',
              4: '/images/grade_4.png',
              5: '/images/grade_5.png'}
  
  rank_info = {90: 5, 80: 4, 50:3, 20:2}
  tier = 0
  for key, value in rank_info.items():
    if final_score >= key:
      tier = value
      break
  if tier == 0:
    tier = 1
  
  res_tier_url = tier_url[tier]
  
  articles = all_article()
  recycling = all_recycling()
  
  article_arr = [article for article in articles]
  recycling_arr = [recycle for recycle in recycling]
  
  article_idx = random.randrange(0, len(article_arr))
  recycling_idx = random.randrange(0, len(recycling_arr))
  
  content_text = article_arr[article_idx].title
  content_image = article_arr[article_idx].image
  content_url = article_arr[article_idx].url
  recycle_tip = recycling_arr[recycling_idx].image
  paritipants = len(all_result())
  
  all_conent = [{'content_text': article.title, 'content_image': article.image, 'content_url': article.url} for article in articles]
  all_recycle_tip = [recycle.image for recycle in recycling]
  ox_list = result_data.ox_list
  
  result = {'user_name': user_name,
            'score': final_score,
            'tier': res_tier_url,
            'tier_value': tier,
            'content_text': content_text,
            'content_image': content_image,
            'content_url': content_url,
            'recycle_tip': recycle_tip,
            'ranking': ranking,
            'participants': paritipants,
            'all_content': all_conent,
            'all_recycle_tip': all_recycle_tip,
            'ox_list': ox_list}
  
  return result
