from datetime import datetime

from get_weather import get_weather, kelvin_to_celsius, get_discomfort_index
from device import *

# 통합시스템

def homeIOT():
    current_weather = get_weather()
    current_time = datetime.now()
    current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    current_logs = []
    
    try:
        # current_home_log = {'datetime': current_time, 'device': '', 'msg': ''}
        light = set_light(current_weather['cloud'])
        print(f"{current_time} device: 조명 {light['status']} {light['msg']}")
        air_con = air_conditioner(current_weather['c_temp'])
        print(f"{current_time} device: 에어컨 {air_con['status']} {air_con['msg']}")
        hum = dehumidifier(current_weather['humidity'])
        print(f"{current_time} device: 제습기 {hum['status']} {hum['msg']}")
        purif = purifier(35, 15)
        print(f"{current_time} device: 공기청정기 {purif['status']} {purif['msg']}")
        mp = music_player(current_weather['cloud'])
        print(f"{current_time} device: 음악플레이어 {mp['status']} {mp['msg']}")
    except Exception as e:
        print("에러 발생! :", e)
        return False
    return True