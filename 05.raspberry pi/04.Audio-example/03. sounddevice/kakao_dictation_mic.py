# 카카오 음성 인식
# 마이크로 5초간 녹음해서 전송
from requests import get, post
import json
import sounddevice as sd
import soundfile as sf
from io import BytesIO
from pydub import AudioSegment, playback
from secret_config import kakao_rest_api_key, weather_api_key

def kakao_recognize(audio):
    kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    headers = {
        "Content-Type": "application/octet-stream",
        "X-DSS-Service": "DICTATION",
        "Authorization": "KakaoAK " + kakao_rest_api_key,
    }

    try:
        res = post(kakao_speech_url, headers=headers, data=audio)
        result_json_string = res.text[
            res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1
        ]
        result = json.loads(result_json_string)
        value = result['value']
        print(f"--- 음성 인식 결과 ---\n{value}\n----------------")
    except:
        value = None
        print("음성 인식 실패")
    return value

def record(seconds=5, fs=16000, channels=1):
    data = sd.rec(int(seconds * fs), samplerate=fs, channels=channels)
    sd.wait()
    audio = BytesIO()
    sf.write(audio, data, fs, format="wav") # format 필수
    audio.seek(0)
    return audio

def get_weather(city='Seoul'):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&lang=kr'
    print(URL)
    weather = {}
    res = get(URL)
    if res.status_code == 200:
        result = res.json()
        weather['main'] = result['weather'][0]['main']
        weather['description'] = result['weather'][0]['description']
        icon = result['weather'][0]['icon']
        weather['icon'] = f'http://openweathermap.org/img/w/{icon}.png'
        weather['etc'] = result['main']
    else:
        print('error', res.status_code)
    return weather

def kakao_synthesize(msg):
    URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    HEADERS = {
        "Content-Type" : "application/xml",
        "Authorization" : f"KakaoAK {kakao_rest_api_key}"
    }
    DATA = f"""
    <speak>{msg}</speak>
    """

    res = post(URL, headers=HEADERS, data=DATA.encode('utf-8'))
    if (res.status_code != 200): # 에러 확인
        print(res, res.text)
    else:
        sound = BytesIO(res.content)
        song = AudioSegment.from_mp3(sound)
        playback.play(song)

if __name__ == '__main__':
    audio = record()
    value = kakao_recognize(audio)

    # 날씨 요청
    weather_string_candidate = ("날씨 알려줘", "날씨", "날씨 어때", "오늘 날씨", "오늘 날씨 어때")
    if value in weather_string_candidate:
        weather = get_weather()
        print(json.dumps(weather, indent=4, ensure_ascii=False)) # utf8 사용
        description = weather['description']
        temp = weather['etc']['temp'] - 273.15
        msg = f"날씨는 {description}! 이고, \
                기온은 {temp:.1f}! 도 입니다."
        kakao_synthesize(msg)
