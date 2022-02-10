import discord
import json
import datetime

TOKEN = ""
channel_id = 

client = discord.Client()
dt = datetime.datetime.now()

f = open('list.json', 'r')
data = json.load(f)

@client.event
async def on_ready():
    print("The bot started successfully.")
    channel = client.get_channel(channel_id)
    for birth in data:
        if int(birth['date']) == dt.month*100+dt.day:
            await channel.send(f"<@{birth['id']}>、お誕生日おめでとうございます🎉🎂")
    exit()

client.run(TOKEN)