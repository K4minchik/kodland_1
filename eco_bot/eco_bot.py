import discord, asyncio, random, os, sqlite3, json, random, datetime
from discord import Color
from discord.ext import commands, tasks
from discord.utils import get

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='%', description=description, intents=intents)
bot.remove_command("help")

videos = ["https://www.youtube.com/watch?v=DkMe3lD6fxk", "https://www.youtube.com/watch?v=t9o-Y2cAYg4", "https://www.youtube.com/watch?v=MRxUrW2ag54"]
items = {"металл": ["алюминиевая банка", "консервная банка", "металлическая крышка", "конструкция из стали", "инструменты", "металлическая упаковка", "провода", "сковорода", "кастрюля"], 
        "пластик": ["пластиковая бутылка", "флакон от бытовой химии", "флакон от шампуня", "канистра", "полиэтиленовый пакет", "шариковая ручка", "одноразовая посуда", "игрушки"],
        "стекло": ["стелянная бутылка", "стеклянная банка", "пузырёк", "посуда", "бокал", "рюмка", "тара", "плита"],
        "органика": ["кожура", "садовые отходы", "овощи", " фрукты", "испорченное мясо", "кости", "молочные продукты", "выпечка"],
        "бумага": ["макулатура", "газеты", "картон", "типографские изделия", "деловые бумаги", "документы", "журналы", "книги", "бумажная упаковка"]}

stop = False
points = 0


@bot.event
async def on_ready():
    """Если бот зашел в сеть"""
    print(f'Бот {bot.user} (ID: {bot.user.id}), готов к работе!')
    print('------')

    channel = bot.get_channel(1152899806570754120)
    emb = discord.Embed(title="Немного боте о Eco", color=(1))
    emb.add_field(name="Привет! Я Eco, занимаюсь экологией.", value="Мой префикс для комманд - **%**\n Префикс это начало комманд, к примеру комманда - **%help**\n", inline=False)
    await channel.send(embed=emb)
    await channel.send("https://tenor.com/view/tree-earth-mother-earth-gif-13083779")


# Игры?
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    
    """Игра о сортировке мусора на время"""
    if message.content.startswith("%sortingame"):
        
        emb=discord.Embed(title="Нам нужна помощь в сортировке мусора.", colour=discord.Color.yellow())
        emb.add_field(name="    ", value="Я пишу тебе предмет, а ты пишешь куда его направить: \n**стекло, металл, пластик, органика, бумага** \nУ тебя будет **30 секунд**! \nНапиши **'старт'**, чтобы начать!", inline=False)
        await message.channel.send(embed=emb)

        def check(message):
            print(message.content.lower())
            return message.content.lower() == 'старт'
        await bot.wait_for("message", check=check)

        await message.channel.send("Начинаем")
        @tasks.loop(seconds=30, count=1)
        async def timer():
            print(timer.current_loop)

        @timer.after_loop
        async def after_timer():
            global stop, points
            stop = True
            if points > 5:
                await message.channel.send(embed=discord.Embed(description=f'Хорошо поработали! Ты набрал **{points}** очков! Не хочешь работать с нами?', colour=discord.Color.green()))
            else:
                await message.channel.send(embed=discord.Embed(description=f'Ух.. Ты набрал **{points}** очков.. Этого маловато! Попробуй ещё раз!', colour=discord.Color.red()))
            points = 0
            stop = False


        timer.start()
        while stop == False: # тута где-то проблемы
            classs = random.choice(list(items))
            item = random.choice(items[classs])
            await message.channel.send(item)
            def check(message):
                print(message.content.lower())
                if message.content.lower() == classs:
                    global points
                    points += 1
                    return message.content.lower() == classs
                else:
                    return message.content.lower() != classs
            await bot.wait_for("message", check=check)
        

            


# Информационные команды
@bot.command()
async def plastic(ctx):
    """Идеями для поделок из бытового пластика"""
    await ctx.send("Держи видео с идеями для поделок из бытового пластика")
    await ctx.send(random.choice(videos))

@bot.command()
async def sorting(ctx):
    """Подсказывает, какие предметы можно  отдавать на переработку"""
    emb = discord.Embed(title="Что можно сдавать на повторную переработку", color=(1))
    emb.add_field(name="Металл", value="алюминиевые и консервные банки, металлические крышки", inline=False)
    emb.add_field(name="Стекло", value="бутылки и банки (из-под напитков и еды), пузырьки и флаконы", inline=False)
    emb.add_field(name="Одежда и обувь", value="кожа, шерсть, мех, текстильные отходы с хорошей тканевой основой", inline=False)
    emb.add_field(name="Бумага", value="картон без примесей, газеты, журналы, открытки, книги, упаковка, офисная бумага", inline=False)
    emb.add_field(name="Электроника", value="в разобранном на пластик, металлы (включая драгоценные) и стекло виде", inline=False)
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

# Общие
@bot.command()
async def clear(ctx, amount = 100):
    """Очистить чат"""
    await ctx.channel.purge(limit=amount)

@bot.command()
async def info(ctx):
    """Инфа о боте"""
    emb = discord.Embed(title="Немного боте о Eco", color=(1))
    emb.add_field(name="Привет! Я Eco, занимаюсь экологией.", value="Мой префикс для комманд - **%**\n Префикс это начало комманд, к примеру комманда - **%help**\n", inline=False)
    await ctx.send(embed=emb)
    await ctx.send("https://tenor.com/view/tree-earth-mother-earth-gif-13083779")

@bot.command()
async def help(ctx):
    """Help"""
    emb = discord.Embed(title="Комманды Eco", color=(1))
    emb.add_field(name="================ Общие команды ===============", value="")
    emb.add_field(name="%help", value="Выводит информацию о командах", inline=False)
    emb.add_field(name="%info", value="Информация о боте", inline=False)
    emb.add_field(name="%clear", value="Очищает чат", inline=False)

    emb.add_field(name="================== Информация ================", value="")
    emb.add_field(name="%plastic", value="Идеями для поделок из бытового пластика", inline=False)
    emb.add_field(name="%sorting", value="Подсказывает, какие предметы можно \nотдавать на переработку", inline=False)
    emb.add_field(name="%decay", value="Рассказывает пользователям сколько разлагается \nтот или иной бытовой предмет", inline=False)

    emb.add_field(name="==================== Игры =====================", value="")
    emb.add_field(name="%sortingame", value="Игра о сортировке мусора на время", inline=False)
    await ctx.send(embed=emb)
    

bot.run("MTE2MDUxMzkyNTIzMDYyODg5NA.G0dR9E.IzbUjDIs-sHKMgTKs6Zp9BPon-qKeOVSq_gjtM")