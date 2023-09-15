from domain.dao.userDao import all_user

def get_user():
  user_data = all_user()
  result = []
  for user in user_data:
    result.append({'id':user.id, 'name':user.name})
  return result