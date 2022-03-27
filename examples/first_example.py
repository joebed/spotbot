import discord
from specials import TOKEN, LOGGER

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('lmao'):
        user = message.author
        await message.channel.send(f'BROOOOO SO FUNNNY')

    if user.mentioned_in(content.message):
        await message.channel.send(f'BROOOOO SO FUNNNY')
    
    
    
    # if message.content_type == image/png:
    #     await message.channel.send(f'Get a load of this guy')

    #If @nick is said, clown on him

client.run(TOKEN)
