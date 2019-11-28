import discord
import asyncio
import requests
import random
import decimal
from discord.utils import get
import cv2 as cv
import Constants
import ParseCommand


client = discord.Client()
@client.event
async def on_ready():
    @client.event
    async def on_message(message):
        member = message.author
        await client.send_message(message.channel, ParseCommand.parse(message.content))

client.run(Constants.AuthToken, bot=True)
