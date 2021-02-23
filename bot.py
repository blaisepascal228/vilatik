from twitchio.ext import commands
import random
import pyimgur
import os
from datetime import datetime

random.seed(datetime.now())

DIR = '' # путь до папки со скринами C:\\bot\\img  именно по два слеша!!!
CLIENT_ID = "77068d52275409d"
im = pyimgur.Imgur(CLIENT_ID)

haha = [':)', ':D', 'авыолщвщалвзщав', 'хаххвхвхвхх']
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='oauth:vb3vwsguxb24oupn6w483o6x32szxx', client_id=None, nick='bot_vilat', prefix='!',
                         initial_channels=['gruccv'])

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        if (message.author.name.lower() == 'bot_vilat'):
            return
        await self.handle_commands(message)

        if ((message.author.name.lower() == 'anonimer22215536') and (len(message.content) > 45)):
            if (random.random() < 0.3):
                await message.channel.send(random.choice(haha))
            else:
                await message.channel.send(message.content)
                
    @commands.command(name='screen')
    async def my_command(self, ctx):
        PATH = os.path.join(DIR, random.choice(os.listdir(DIR)))
        uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
        await ctx.send(uploaded_image.link)         

bot = Bot()
bot.run()

