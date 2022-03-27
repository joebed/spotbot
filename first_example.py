import discord
from specials import TOKEN, LOGGER

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_attachment(attachment):
    if attachment.author == client.user:
        return
    print(type(attachment))
    print(str(attachment.content_type))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.attachments)
    for attach in message.attachments:
        print(type(attach))
        print(attach.content_type)
        if attach.content_type.startswith('image'):
            await message.channel.send(f'Can you send it again my eyes were closed')
    
    if 'lmao' in message.content:
        await message.channel.send(f'BROOOOO SO FUNNNY')

    if "ben" in message.content:
        await message.channel.send(":eggplant:")

    if "ring" in message.content:
        await message.channel.send(":peach:")
        
    if "nick" in message.content:
        await message.channel.send(f'Get a load of this guy')

    if message.author.display_name == "KCIN75":
        await message.channel.send(f'Nick knock it off')

    elif message.author.display_name == "shel":
        await message.channel.send(f'Please elaborate sheldon')
    
    elif message.author.display_name == "Aymin":
        await message.channel.send(f'Aymin, that is a very pleasant wordle; however, I got mine in 2')
    
    elif message.author.display_name == "Gabe Renaud":
        await message.channel.send(f'Daddy Gabe :heart_eyes:')
    
    elif message.author.display_name == "habibi":
        await message.channel.send(f'Martin congratulations you have won .27 BTC!')
        
    elif message.author.display_name == "DelusionalTaco72":
        await message.channel.send(f'Wdym?')
        
    elif message.author.display_name == "jabapo":
        await message.channel.send(f'How\'s my form?')
        
    if "gn" in message.content:
        await message.channel.send(f'Baby please don\'t hang up i love you so much')
    

client.run(TOKEN)
