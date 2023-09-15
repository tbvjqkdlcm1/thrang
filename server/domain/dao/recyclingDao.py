from domain.models.recycling import Recycling

def all_recycling():
  result = Recycling.query.all()
  return result