import pyrogram
from pyrogram import Client, filters
from pyrogram.filters import command
import asyncio
import random
from patterns import *
from patterns import _heart
"""
data.py must be like:
api_id = api_id (int)
api_hash = "api_hash" (str)
"""
from data import api_id, api_hash

time_sleep = 0.25
avaliable_hearts = ["🧡", "💚", "💙", "💝", "💘", "💖", "🖤"]

app = Client(
            'heartUserbot',
            api_id=api_id,
            api_hash=api_hash
        )


@app.on_message(command('❤️', prefixes='') & filters.me)
async def send_heart(app, msg):
    heart = _heart
    nickname = msg.text.split()[1]
    result = ""
    for i in range(3):
        result = arr2d2str(heart)
        await msg.edit(result.replace(yellow, avaliable_hearts[i]))
        await asyncio.sleep(time_sleep)
        result = ""
        
    for i in range(10):
        result = arr2d2str(heart)

        try:
            await msg.edit(result)
        except pyrogram.errors.exceptions.bad_request_400.MessageNotModified:
            pass

        await asyncio.sleep(time_sleep)
        for i in range(len(heart)):
            for j in range(len(heart[i])):
                if heart[i][j] != white and heart[i][j] != red:
                    heart[i][j] = random.choice(avaliable_hearts)
                else:
                    continue
        if i < 4:
            result = ""

    counter = 10
    while counter > 0:
        del heart[counter]
        for el in heart:
            del el[-1]
        await msg.edit("{}".format(arr2d2str(heart)))
        await asyncio.sleep(time_sleep)
        counter -=1

    await msg.edit(f"Я люблю тебя, {nickname}")


app.run()
