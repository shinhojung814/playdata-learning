"""
Openweather API 의 current weather 불러오는 엔드포인트 사용
도시는 서울 기준
리턴값 형태
code: 요청 성공 여부
c_temp: 섭씨 온도
humidity: 습도
discomfort_index: 불쾌지수
: 명도는 구름량으로 대체
: 미세먼지
"""

import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=seoul&appid=2b19e69e526690082e7f29d31f21137f"


def kelvin_to_celsius(temperature):
    return round(temperature - 273.15, 2)

def get_discomfort_index(c_temp, hum):
    # 원래 상대습도를 써야하나 편의상 습도 사용
    return ( (9/5 * c_temp) - (0.55 * (1 - hum) * ( (9/5 * c_temp) - 26 ) + 32 ))

def get_weather():
    res = requests.get(url)
    result = {}
    if res.status_code == 200:
        result["code"] = True
        res = res.json()
        result['c_temp'] = kelvin_to_celsius(res['main']['temp'])
        result['humidity'] = res['main']['humidity']
        result['discomfort_index'] = get_discomfort_index(result['c_temp'], result['humidity'])
        result['cloud'] = res['clouds']['all']
        result['particulate_matter'] = 20
    else:
        result["code"] = False
    return result

if __name__ == "__main__":
    print(get_weather())
