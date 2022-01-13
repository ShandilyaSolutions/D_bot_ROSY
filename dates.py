import requests
import json

def get_data(month, date):
    url = "http://history.muffinlabs.com/date/%s/%s"%(month, date)
    response = requests.get(url)
    data = json.loads(response.text)
    req_data = {}
    for i in data["data"]["Events"]:
        if i["year"] in req_data:
            req_data[i["year"]].append(i["text"])
        else:
            req_data[i["year"]]= [i["text"]]   
    return req_data

if __name__ == "__main__":
    data = get_data(1, 1)
    for i in data:
        for j in data[i]:
            print(i, ":", j)
