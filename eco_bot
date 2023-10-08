import discord, asyncio, random, os
from discord.ext import commands
from discord.utils import get

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)
bot.remove_command("help")

videos = ["https://www.youtube.com/watch?v=DkMe3lD6fxk", "https://www.youtube.com/watch?v=t9o-Y2cAYg4", "https://www.youtube.com/watch?v=MRxUrW2ag54"]

@bot.event
async def on_ready():
    """Если бот зашел в сеть"""
    print(f'Бот {bot.user} (ID: {bot.user.id}), готов к работе!')
    print('------')

    channel = bot.get_channel(1152899806570754120)
    emb = discord.Embed(title="Немного боте о Eco", color=(1))
    emb.add_field(name="Привет! Я Eco, занимаюсь экологией.", value="Мой префикс для комманд - $\n Префикс это начало комманд, к примеру комманда - $help\n", inline=False)
    await channel.send(embed=emb)
    await channel.send("https://tenor.com/view/tree-earth-mother-earth-gif-13083779")
    
@bot.command()
async def clear(ctx, amount = 100):
    """Очистить чат"""
    await ctx.channel.purge(limit=amount)

@bot.command()
async def plastic(ctx):
    """Идеями для поделок из бытового пластика"""
    await ctx.send("Держи с идеями для поделок из бытового пластика")
    await ctx.send(random.choice(videos))

@bot.command()
async def sorting(ctx):
    """Подсказывает, какие предметы можно выбрасывать в обычную урну, а какие стоит отдавать на переработку"""
    emb = discord.Embed(title="Что можно сдавать на повторную переработку", color=(1))
    emb.add_field(name="Металл", value="алюминиевые и консервные банки, металлические крышки", inline=False)
    emb.add_field(name="Стекло", value="бутылки и банки (из-под напитков и еды), пузырьки и флаконы", inline=False)
    emb.add_field(name="Одежда и обувь", value="кожа, шерсть, мех, текстильные отходы с хорошей тканевой основой", inline=False)
    emb.add_field(name="Бумага", value="картон без примесей, газеты, журналы, открытки, книги, упаковка, офисная бумага", inline=False)
    emb.add_field(name="Электроника", value="бутылки и банки (из-под напитков и еды), пузырьки и флаконы", inline=False)
    emb.add_field(name="Пластик", value="бутылки, флаконы от бытовой химии и шампуней, канистры, пластиковые бутылки от молочной продукции маркировки 1,2 (только этот вид пластика будет переработан)", inline=False)
    await ctx.send(embed=emb)

@bot.command()
async def decay(ctx):
    """Рассказывает пользователям сколько разлагается тот или иной бытовой предмет"""
    emb = discord.Embed(title="Сколько времени разлагаются бытовые отходы", color=(1))
    emb.add_field(name="Бумага", value="5 лет", inline=False)
    emb.add_field(name="Губка для мытья посуды или полиэтиленового пакет", value="более 200 лет", inline=False)
    emb.add_field(name="Фольга или пластиковая бутылка", value="100 лет", inline=False)
    emb.add_field(name="Автомобильная покрышка", value="140 лет", inline=False)
    emb.add_field(name="Стекло", value="более 1000 лет", inline=False)
    await ctx.send(embed=emb)
    

@bot.command()
async def info(ctx):
    """Инфа о боте"""
    emb = discord.Embed(title="Немного боте о Eco", color=(1))
    emb.add_field(name="Привет! Я Eco, занимаюсь экологией.", value="Мой префикс для комманд - $\n Префикс это начало комманд, к примеру комманда - $help\n", inline=False)
    await ctx.send(embed=emb)
    await ctx.send("https://tenor.com/view/tree-earth-mother-earth-gif-13083779")

@bot.command()
async def help(ctx):
    """Help"""
    emb = discord.Embed(title="Комманды Eco", color=(1))
    emb.add_field(name="$help", value="Выводит информацию о командах", inline=False)
    emb.add_field(name="$plastic", value="Идеями для поделок из бытового пластика", inline=False)
    emb.add_field(name="$sorting", value="Подсказывает, какие предметы можно выбрасывать в обычную урну, а какие стоит отдавать на переработку", inline=False)
    emb.add_field(name="$decay", value="Рассказывает пользователям сколько разлагается тот или иной бытовой предмет", inline=False)
    emb.add_field(name="$info", value="Информация о боте", inline=False)
    emb.add_field(name="$clear", value="Очищает чат", inline=False)
    await ctx.send(embed=emb)
    

bot.run("TOKEN")
