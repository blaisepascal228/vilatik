from twitchio.ext import commands
import random
import pyimgur

haha = ['1352131312312412131213', ':)', ':D',
        '69090789789787979', 'авыолщвщалвзщав', 'хаххвхвхвхх']


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='oauth:vb3vwsguxb24oupn6w483o6x32szxx', client_id=None, nick='bot_vilat', prefix='!',
                         initial_channels=['gruccv'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        if (message.author.name.lower() == 'bot_vilat'):
            return
        await self.handle_commands(message)

        if ((message.author.name.lower() == 'pascalblaise') and (len(message.content) > 3)):
            if (random.random() < 0.3):
                await message.channel.send(random.choice(haha))
            else:
                await message.channel.send(message.content)

    # Commands use a decorator...

    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()
