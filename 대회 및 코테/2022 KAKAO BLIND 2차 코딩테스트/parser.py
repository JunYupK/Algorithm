import requests
headers = {'User-Agent' : 'Mozillas/5.0'}
timeout = 5
res = requests.get('https://www.naver.com/',headers=headers, timeout=timeout)
print(res.status_code)
# print(res.headers)
print(res.content)
# print(res.cookies)