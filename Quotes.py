import requests
import json

def get_quotes():
    url = "https://zenquotes.io/api/random"

    response = requests.get(url)

    data = json.loads(response.text)
    
    req = {}

    req['q']=data[0]['q']
    req['a']=data[0]['a']

    return req



if __name__ == '__main__':
    quote = get_quotes()
    print(quote)
