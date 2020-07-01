from datetime import datetime

from weather import kelvin_to_celsius, get_discomfort_index, get_weather
from device import *

# 통합시스템

def homeIOT():
    current_weather = get_weather()
    current_time = datetime.now()
    current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    current_logs = []
    result = {}
    
    try:
        light = set_light(current_weather['cloud'])
        light_log = f"{current_time} device: 조명 {light['status']} {light['msg']}"
        current_logs.append(light_log)

        air_con = air_conditioner(current_weather['c_temp'])
        air_conditioner_log = f"{current_time} device: 에어컨 {air_con['status']} {air_con['msg']}"
        current_logs.append(air_conditioner_log)
        
        hum = dehumidifier(current_weather['humidity'])
        hum_log = f"{current_time} device: 제습기 {hum['status']} {hum['msg']}"
        current_logs.append(hum_log)
        
        purif = purifier(35, 15)
        purif_log = f"{current_time} device: 공기청정기 {purif['status']} {purif['msg']}"
        current_logs.append(purif_log)
        
        mp = music_player(current_weather['cloud'])
        mp_log = f"{current_time} device: 음악플레이어 {mp['status']} {mp['msg']}"
        current_logs.append(mp_log)
        result['code'] = True
    
    except Exception as e:
        print("에러 발생! :", e)
        error_log = f"{current_time} {str(e)}"
        current_logs.append(error_log)
        result['code'] = False
        
    result['logs'] = current_logs
    return result
