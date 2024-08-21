import requests
# serviceKey='93kx6v969%2BmW0CuYPqJRzr2NNLyrnvyjc%2FvGGW%2Bpu5jye%2Bsq%2BczIl9j%2BPiFf92jiUnAdh9%2FJ1%2B%2FWwml5bNU1Dg%3D%3D'
serviceKey='93kx6v969+mW0CuYPqJRzr2NNLyrnvyjc/vGGW+pu5jye+sq+czIl9j+PiFf92jiUnAdh9/J1+/Wwml5bNU1Dg=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '울산', 'ver' : '1.0' }

response = requests.get(url, params=params)
air=response.json()
print(air)