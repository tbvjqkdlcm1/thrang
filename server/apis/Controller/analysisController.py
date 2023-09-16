from flask import Blueprint, request
from apis.dto.requestDto import analysis_request_dto
from apis.dto.responseDto import analysis_response_dto
from service.analysisService import analysis_service

analysis_bp = Blueprint('analysis', __name__, url_prefix='/api')

@analysis_bp.route('/analysis', methods=['POST'])
def get_analysis_result():
  analysis_data = analysis_request_dto(request.get_json())
  user_id = analysis_service(analysis_data) # 결과 분석 후 유저의 아이디 리턴

  return analysis_response_dto(user_id)