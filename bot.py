import discord
from discord.ext import commands
import requests
import os

TOKEN = os.getenv("DISCORD_TOKEN")
USERNAME = os.getenv("ATERNOS_USER")
PASSWORD = os.getenv("ATERNOS_PASS")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def start(ctx):
    await ctx.send("جاري تشغيل السيرفر...")
    session = requests.Session()
    login = session.post("https://aternos.org/ajax/account/login", data={
        "user": USERNAME,
        "password": PASSWORD
    })
    if "ok" in login.text:
        session.get("https://aternos.org/:server/")
        start = session.post("https://aternos.org/ajax/server/start")
        if "ok" in start.text:
            await ctx.send("تم تشغيل السيرفر بنجاح!")
        else:
            await ctx.send("فشل تشغيل السيرفر.")
    else:
        await ctx.send("فشل تسجيل الدخول لـ Aternos.")

bot.run(TOKEN)
