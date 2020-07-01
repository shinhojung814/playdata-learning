def set_light(x):
    for i in range(x):
        if 0 <= x and x < 30:
            light = 1
        elif 30 <= x and x < 60 :
            light = 2
        elif 60 <= x and x < 85:
            light = 3
        elif 85 <= x and x <= 100:
            light = 3
        else:
            light = 0
            return {'status':'OFF', 'msg':'조명을 끕니다.'}
    return {'status':'ON' ,'msg':'%d단계 조명을 킵니다.' % light}

status = 'status'
msg = 'msg'
#에어컨 관련 함수들

#에어컨 전원함수
def aircon_power(a):
  if a == 'on':
   return {status : 'on',  msg : '에어컨을 가동합니다.'}
  else: 
    pass

#에어컨 온도설정 함수
def aircon_temp(a):
  if a >= 28:
     return {status : 'on',  msg : '에어컨온도를 22도로 설정합니다.'}
  elif a <= 22:
     return {status : 'on',  msg : '에어컨온도를 26도로 설정합니다.'}
  elif 22 < a < 28:
     return {status : 'on',  msg : '에어컨을 계속 가동합니다.'}
  else:
    pass

#에어컨 함수
def air_conditioner(temp): 
 if temp >= 28:  
  return aircon_temp(temp)
 elif 22 < temp < 28:
    if aircon_power('on') == 'on':
       return aircon_temp(temp)
    elif aircon_power('on') != 'on':
       return {status : 'off',  msg : '에어컨을 가동하지 않습니다.'}
 else:
    return { status : 'off',  msg :'에어컨을 가동하지 않습니다.'}

#제습기 관련함수들

#제습기 전원함수
def dehumidifier_power(a):
  if a == 'on':
    return {status : 'on',  msg : '제습기를 가동합니다.'} 
  else: 
    pass

#제습기 습도설정 함수
def dehum_hum(a):
  if a >= 60:
     return {status : 'on',  msg : '제습기 습도를 40%로 설정합니다.'}
  elif a <= 40:
     return {status : 'on',  msg : '제습기 습도를 50%로 설정합니다.'} 
  elif 40 < a < 60:
     return {status : 'on',  msg : '제습기를 계속 가동합니다.'} 
  else:
    pass

#제습기 함수
def dehumidifier(hum): 
 if hum >= 60:
    return dehum_hum(hum)
 elif 40 < hum < 60:
    if dehumidifier_power('on') == 'on':
      return dehum_hum(hum)
    elif dehumidifier_power('on') != 'on':
      return {status : 'off',  msg :'제습기를 가동하지 않습니다.'}
 else:
    return { status : 'off',  msg :'제습기를 가동하지 않습니다.'}

# 플레이리스트 함수
def music_on(y):
    if y == 'on':
        return {status : 'on' , msg : '플레이리스트를 찾는 중입니다.'}

def music_player(cloud):
        if 0 < cloud < 30:
            return {status: 'on',msg : '화창한 날 듣기 좋은 음악입니다' }
        elif 30 <= cloud < 70:
            return {status: 'on' , msg : '흐린 날 듣기 좋은 음악입니다'}
        else:
            return {status: 'on' , msg : '비 오는 날 듣기 좋은 음악입니다'}
            
def purifier(pm10, pm25):

    status = ['좋음', '보통', '나쁨', '매우 나쁨']
    
    if pm10 < 30:
        msg1 = status[0]
    elif pm10 < 80:
        msg1 = status[1]
    elif pm10 < 150:
        msg1 = status[2]
    else:
        msg1 = status[3]

    if pm25 < 15:
        msg2 = status[0]
    elif pm25 < 35:
        msg2 = status[1]
    elif pm25 < 75:
        msg2 = status[2]
    else:
        msg2 = status[3]

    if msg1 in status[2:]:
        return {'status': 'ON', 'msg': '공기청정기를 작동합니다.'}
    else:
        if msg2 in status[2:]:
            return {'status': 'ON', 'msg': '공기청정기를 작동합니다.'}
        else:
            return {'status': 'OFF', 'msg': '공기청정기를 작동하지 않습니다.'}
