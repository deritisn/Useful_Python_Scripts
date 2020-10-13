import requests
import json

def API_call():
    #for baseUrl, always copy what is left of the ? for the API call
    URL = 'https://api.upcitemdb.com/prod/trial/lookup'
    parameters = {'upc': '012993441012'}
    response = requests.get(URL, params= parameters)
    print(response.url)

    content = response.content
    info = json.loads(content)

    item = info['items']
    itemInfo = item[0]
    title = itemInfo['title']
    brand = itemInfo['brand']
    print(title)
    print(brand)

API_call()
