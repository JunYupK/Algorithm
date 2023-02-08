import requests

BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
HEADERS = {'X-Auth-Token': '403cd601434042db7430978d9a20d109'}
TIMEOUT = 5


def startAPI(data):
    DATA = {'problem': int(data)}
    res = requests.post(BASE_URL + '/start', data=DATA, headers=HEADERS, timeout=TIMEOUT)
    return res.json()


def waitingLineAPI(key):
    getHeader = {'Authorization': key}
    res = requests.get(BASE_URL + '/waiting_line', headers=getHeader, timeout=TIMEOUT)
    return res.json()


def gameResultAPI(key):
    getHeader = {'Authorization': key}
    res = requests.get(BASE_URL + '/game_result', headers=getHeader, timeout=TIMEOUT)
    return res.json()


def userInfoAPI(key):
    getHeader = {'Authorization': key}
    res = requests.get(BASE_URL + '/user_info', headers=getHeader, timeout=TIMEOUT)
    return res.json()


def matchAPI(key, pairs):
    getHeader = {'Authorization': key}
    res = requests.put(BASE_URL + '/match', json={'pairs': pairs}, headers=getHeader)
    return res.json()


def scoreAPI(key):
    getHeader = {'Authorization': key}
    res = requests.get(BASE_URL + '/score', headers=getHeader)
    print(res.json())
    return res.json()


def gameResultAPI(key):
    getHeader = {'Authorization': key}
    res = requests.get(BASE_URL + '/score', headers=getHeader)
    print(res.json())
    return res.json()
