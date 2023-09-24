import discord, asyncio, random
from discord.ext import commands, tasks
from bot_logic import *

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='%', description=description, intents=intents)
bot.remove_command("help")

hello_words = ['привет', "хай", 'здравствуй', 'добрый день', 'добрый вечер', 'доброе утро']
bye_words = ["пока", "прощай", "досвидания", "до свидания", "бай"]
bad_words = ["обезьяны", "обезьяна", "лысый", "версус", "немощь"]

@bot.event
async def on_ready():
    print(f'Бот {bot.user} (ID: {bot.user.id}), готов к работе!')
    print('------')

    channel = bot.get_channel(1152899806570754120)
    emb1 = discord.Embed(title="Немного боте о LegoEda", color=(1))
    emb1.add_field(name="Привет! Я бот по фандому TOH (The Owl House)", value="Мой префикс для комманд - %\n Префикс это начало комманд, к примеру комманда - %help\n Надеюсь я тебе понравлюсь!", inline=False)
    #потом будет выводиться гифка где она танцует
    await channel.send(embed=emb1)
    

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return

    msg = message.content.lower()

    find_bad_words = False
    for item in bad_words:
        if msg.find(item) >= 0:
            find_bad_words = True
    if find_bad_words:
        await message.channel.send("Осуждаю такие слова.")

    find_hello_words = False
    for item in hello_words:
        if msg.find(item) >= 0:
            find_hello_words = True
    if find_hello_words and find_bad_words == False:
        await message.channel.send("Хаай! Чего хочешь человек?")

    find_bye_words = False
    for item in bye_words:
        if msg.find(item) >= 0:
            find_bye_words = True
    if find_bye_words and find_bad_words == False:
        await message.channel.send("Было приятно пообщаться! Байииии!")

    if "как дела" in message.content.lower() and find_bad_words == False:
        await message.channel.send("Отлично! Сижу, пью яблочную кровь.")

@bot.command()
async def password(ctx, pass_length = 10):
    """Генератор пароля"""
    await ctx.send(gen_pass(pass_length))

@bot.command()
async def coin(ctx):
    """Жребий"""
    await ctx.send(f"Бросаю монету :coin:")
    #потом здесь будет гифка с монетой
    delay = random.uniform(3, 6)
    await asyncio.sleep(delay)
    await ctx.send(f"{flip_coin()}  {gen_emoji()}")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Говорит когда кто-то зашел на сервер"""
    await ctx.send(f'{member.name} вошёл на сервер {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def clear(ctx, amount = 100):
    """Очистить чат"""
    await ctx.channel.purge(limit=amount)

@bot.command()
async def info(ctx):
    """Инфа о боте"""
    emb1 = discord.Embed(title="Немного боте о LegoEda", color=(1))
    emb1.add_field(name="Привет! Я бот по фандому TOH (The Owl House)", value="Мой префикс для комманд - %\n Префикс это начало комманд, к примеру комманда - %help\n Надеюсь я тебе понравлюсь!", inline=False)
    #потом здесь будет гифка где ида танцует
    await ctx.send(embed=emb1)

@bot.command()
async def help(ctx):
    """Help"""
    emb = discord.Embed(title="Комманды LegoEda", color=(1))

    emb.add_field(name="%help", value="Выводит информацию о командах", inline=False)

    emb.add_field(name="%password ЧИСЛО_СИМВОЛОВ", value="Генерирует пароль", inline=False)
    emb.add_field(name="%coin", value="Жребий", inline=False)
    emb.add_field(name="%joined @ПОЛЬЗОВАТЕЛЬ", value="Выводит когда зашёл на сервер указанный пользователь", inline=False)
    emb.add_field(name="%clear", value="Очищает чат", inline=False)
    emb.add_field(name="%info", value="Очищает чат", inline=False)
    
    await ctx.send(embed=emb)


bot.run("MTE1MjkwMDAyNTc4NjA1MjcyOA.GrjTkq.yFgtsDi5oJLIBq_IXrXJS2ZqsZjFAZ5MxYxcv0")
