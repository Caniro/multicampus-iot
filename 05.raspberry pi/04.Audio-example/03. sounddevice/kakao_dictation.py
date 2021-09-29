# 카카오 음성 인식
import requests
import json
from secret_config import kakao_rest_api_key

kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + kakao_rest_api_key,
}

# 파일 내용을 전송
filename = ('heykakao.wav', 'hivixby.wav', 'errorcase.wav')[0]
with open(filename, 'rb') as fp:
    audio = fp.read()
    res = requests.post(kakao_speech_url, headers=headers, data=audio)
    # print(res.text)

# finalResult 추출
try:
    result_json_string = res.text[
        res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1
    ]
    result = json.loads(result_json_string)
    value = result['value']
    print(f"--- 음성 인식 결과 ---\n{value}")
except:
    print("음성 인식 실패")

# 파이썬 문법) 찾는 문자열이 없을 경우
# string.index() : 없으면 예외 발생
# string.find() : 없으면 -1 리턴
