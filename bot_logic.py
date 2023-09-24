import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emoji():
    emoji = [":weary:", ":face_holding_back_tears:", ":laughing:", ":japanese_goblin:"]
    return random.choice(emoji)


def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Выпал орёл"
    else:
        return "Выпала решка"

