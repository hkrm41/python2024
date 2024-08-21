import requests
serviceKey='93kx6v969+mW0CuYPqJRzr2NNLyrnvyjc/vGGW+pu5jye+sq+czIl9j+PiFf92jiUnAdh9/J1+/Wwml5bNU1Dg=='
url = 'http://openapi.its.ulsan.kr/UlsanAPI/BusstopOnOff.xo'
params ={'serviceKey' : serviceKey, 'pageNo' : 'json', 'numOfRows' : '10', 'stopName' : '공업탑', 'basicDay' : '20160301' }

response = requests.get(url, params=params)
air=response.text
print(air)      