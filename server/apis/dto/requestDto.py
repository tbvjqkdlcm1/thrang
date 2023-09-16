def analysis_request_dto(result):
    return {
        "user_name": result['user_name'], 
        "answers": result['answers'], 
        "start_time": result['start_time'],
        "end_time": result['end_time'],
        "delivery_count": result['delivery_count']
    }