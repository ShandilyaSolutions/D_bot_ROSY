import requests
import os
import json

#more work needed

key=os.environ['API_KEY']


msg={}
def getWeatherOfBanglore():
  url = "http://api.openweathermap.org/data/2.5/weather?lat=12.9716&lon=77.5946&units=metric&appid=%s"%(key)

  response = requests.get(url)

  data=json.loads(response.text)
  #print(data)

  msg="Weather Condition : "+str(data['weather'][0]['main'])+'\n'+"Temperature  : "+str(data['main']['temp'])+"\n"+"Feels Like  : "+str(data['main']['feels_like'])+'\n'

  return(msg)
if __name__=='__main__':
  result=getWeatherOfBanglore()
  print(result)
