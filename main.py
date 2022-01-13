import os
import discord
import random
import dates
import Quotes
import datetime
import weather
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author == client.user:
          return
  
        if message.content.startswith('$hello'):
          #to create more humane replies
          hello=['Greetings sire!','Bonjour!',' How goes it?',"What's up",'Hi!','Buenas Noches','Howdy-do?','Howdy',' Buenos Dias!','Hi-ya','Shalom','Good-day!','How are you?',"What's happening",'Namaste','Namaskara','Halo','Vanakkam']
          message_txt=random.choice(hello)
          await message.channel.send(message_txt)
        
        if message.content.startswith('$help'):
          await message.channel.send('Sorry dude! This part is not ready yet')
        
        if message.content.startswith('$inspire'):
          quote = Quotes.get_quotes()
          await message.channel.send(quote['q']+"  : "+quote['a'])

        if message.content.startswith('$history'):
          msg = message.content
          output=[]
          print(msg)
          lst=msg.split(' ')
          l=len(lst)
          if (l != 3):
            await message.channel.send("Invalid Input, Correct Format  : MM-DD")
            return None
          date = lst[(l-1)]
          month = lst[(l-2)]
          s=["Showing history for %02d/%02d   : \n"%(int(date),int(month))]

          if(not date.isnumeric()) or (not month.isnumeric()):
            await message.channel.send("Invalid Input, Correct Format  : MM-DD")
            return None
          try:
            datetime.datetime.strptime("%02d-%02d-2020"%(int(date), int(month)), "%d-%m-%Y")
          except ValueError:
              await message.channel.send("Invalid Date, Correct Fomat : MM-DD")
              return None
          history = dates.get_data(month,date)
          for k, v in history.items():
            output.append(k+" - "+v[0])
          for i in output:
            if(len(s[-1])+len(i) < 2000):
              s[-1]=s[-1]+str(i)+"\n"
            else:
              s.append("")
              s[-1]=s[-1]+str(i)+"\n"
          for i in s:
            await message.channel.send(i)
        if message.content == '--show available commands':
          #a dictionary of available commands
          commands = {
          '$hello':'for hello message',
          '$help':'for getting help',
          '$history MM-DD' : 'to get a list of historical events occuring on DD/MM',
          '$weatherBlore':'to know the current weather of Banglore city'
          }
          output=''
          for k,v in commands.items():
            output=output+(k+' - '+v)+'\n'
          await message.channel.send(output)
        if message.content.startswith('$weatherBlore'):
          output=weather.getWeatherOfBanglore()
          await message.channel.send(output)

          
keep_alive()
client=MyClient()          
client.run(my_secret)
