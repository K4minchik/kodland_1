import discord, asyncio, random, os
from discord.ext import commands
from discord.utils import get
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
    """Если бот зашел в сеть"""
    print(f'Бот {bot.user} (ID: {bot.user.id}), готов к работе!')
    print('------')

    channel = bot.get_channel(1152899806570754120)
    emb = discord.Embed(title="Немного боте о LegoEda", color=(1))
    emb.add_field(name="Привет! Я бот по фандому TOH (The Owl House)", value="Мой префикс для комманд - %\n Префикс это начало комманд, к примеру комманда - %help\n Надеюсь я тебе понравлюсь!", inline=False)
    await channel.send(embed=emb)
    await channel.send("https://tenor.com/view/lego-eda-eda-toh-the-owl-house-dance-gif-27037017")
    

@bot.event
async def on_message(message):
    """Диалоги"""
    await bot.process_commands(message)
    if message.author == bot.user:
        return

    msg = message.content.lower()

    find_bad_words = False
    for item in bad_words:
        if msg.find(item) >= 0:
            find_bad_words = True
    if find_bad_words:
        await message.channel.send("Осуждаю такие слова :rage:")

    find_hello_words = False
    for item in hello_words:
        if msg.find(item) >= 0:
            find_hello_words = True
    if find_hello_words and find_bad_words == False:
        await message.channel.send(f"Хаай! Чего хочешь человек? {gen_emoji()}")

    find_bye_words = False
    for item in bye_words:
        if msg.find(item) >= 0:
            find_bye_words = True
    if find_bye_words and find_bad_words == False:
        await message.channel.send(f"Было приятно пообщаться! Байииии! {gen_emoji()}")

    if "как дела" in message.content.lower() and find_bad_words == False:
        await message.channel.send(f"Отлично! Сижу, пью яблочную кровь. {gen_emoji()}")

@bot.event
async def on_member_join(member):
    """Если кто-то зашел на сервер"""
    channel = bot.get_channel(1152899806570754120)
    role = discord.utils.get(member.guild.roles, id=1158012500432924693)
    await member.add_roles(role)
    emb = discord.Embed(title = f"Участник {member} зашёл на сервер!", colour = discord.Color.yellow())
    emb.add_field(name="Дата входа", value=(discord.utils.format_dt(member.joined_at)))
    await channel.send(embed=emb)



@bot.command()
async def password(ctx, pass_length = 10):
    """Генератор пароля"""
    if pass_length >= 2001:
        await ctx.send('Слишком много символом, максимум 2000')
    else:
        await ctx.send(gen_pass(pass_length))
        

@bot.command()
async def coin(ctx):
    """Жребий"""
    await ctx.send("https://tenor.com/view/coin-toss-coin-toss-gif-5017733")
    delay = random.uniform(3, 6)
    await asyncio.sleep(delay)
    emb = discord.Embed(title=f"{flip_coin()}", color=(1))
    await ctx.send(embed=emb)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Говорит когда кто-то зашел на сервер"""
    await ctx.send(f'{member.name} вошёл на сервер {discord.utils.format_dt(member.joined_at)}')

@bot.command()
@commands.has_role(1158022812154470481)
async def clear(ctx, amount = 100):
    """Очистить чат"""
    await ctx.channel.purge(limit=amount)

@bot.command()
async def info(ctx):
    """Инфа о боте"""
    emb1 = discord.Embed(title="Немного боте о LegoEda", color=(1))
    emb1.add_field(name="Привет! Я бот по фандому TOH (The Owl House)", value="Мой префикс для комманд - %\n Префикс это начало комманд, к примеру комманда - %help\n Надеюсь я тебе понравлюсь!", inline=False)
    await ctx.send(embed=emb1)
    await ctx.send("https://tenor.com/view/lego-eda-eda-toh-the-owl-house-dance-gif-27037017")

@bot.command()
async def mem(ctx, theme = "None"):
    """Отправляет рандомный мем из категории"""
    if theme == "toh":
        img_names = random.choice(os.listdir('memes_toh'))
        with open(f'memes_toh/{img_names}', 'rb') as f:
            # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
            picture = discord.File(f)
        # Можем передавать файл как параметр!
        await ctx.send(file=picture)
    elif theme == "video":
        img_names = random.choice(os.listdir('memes_video'))
        with open(f'memes_video/{img_names}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        img_names = random.choice(os.listdir('memes'))
        with open(f'memes/{img_names}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def duck(ctx):
    '''Выводит рандомное изображение с утками'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
@commands.has_role(1158022812154470481)
async def mute(ctx, member: discord.Member, time: int):
    """Мутит учасника на кол-во секунд"""
    emb = discord.Embed(title = f"Участник {member} Был Замучен!", colour = discord.Color.red())
    emb.add_field(name="Его замутил ", value=(ctx.author.name))
    emb.add_field(name="Длительность ", value=f"{time}")
    await ctx.send(embed=emb)
    role = discord.utils.get(member.guild.roles, id=1158012500432924693)
    muted_role = discord.utils.get(member.guild.roles, id=1158008825543131296)
    await member.add_roles(muted_role)
    await member.remove_roles(role)

    await asyncio.sleep(time)
    await member.add_roles(role)
    await member.remove_roles(muted_role)
    

@bot.command()
async def help(ctx):
    """Help"""
    emb = discord.Embed(title="Комманды LegoEda", color=(1))
    emb.add_field(name="  Общие команды", value="")
    emb.add_field(name="%help", value="Выводит информацию о командах", inline=False)
    emb.add_field(name="%password ЧИСЛО_СИМВОЛОВ", value="Генерирует пароль (макс. 2000 символов)", inline=False)
    emb.add_field(name="%coin", value="Жребий", inline=False)
    emb.add_field(name="%joined @УЧАСНИК", value="Выводит когда зашёл на сервер указанный пользователь", inline=False)
    emb.add_field(name="%info", value="Информация о боте", inline=False)
    emb.add_field(name="%mem (None, toh, video)", value="Отправляет рандомный мем из категории", inline=False)
    emb.add_field(name="%duck", value="Отправляет рандомную картинку утки", inline=False)

    emb.add_field(name="  Комманды Админа", value="")
    emb.add_field(name="%mute @УЧАСНИК СЕКУНДЫ", value="Мутит учасника на кол-во секунд", inline=False)
    emb.add_field(name="%clear", value="Очищает чат", inline=False)
    await ctx.send(embed=emb)


bot.run("TOKEN")
