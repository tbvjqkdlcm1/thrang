from domain.dao.resultDao import all_result

def get_main_result():
    user_cnt = len(all_result())
    result = {
        'user_cnt':user_cnt
    }
    return result