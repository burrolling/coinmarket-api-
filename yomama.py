import requests
parameters = {'count':'3'}
url = 'https://yomomma-api.herokuapp.com/jokes'
def yomama():
    jokes = []
    json = requests.get(url, params = parameters).json()
    for i in json:
        jokes.append(i["joke"])
    return jokes

