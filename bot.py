import discord
import requests

TOKEN = 'MTI4NTU1MTU0ODIxNDI4NDMxOQ.GVBsa3.iPcwYUjyEVXE6VarUio91LJqFXW6LuJLovJ-cg'
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
