import random


def createPass(length: int, all_standart_symbols: str, custom_symbols="") -> str:
    all_symbols = list(all_standart_symbols + custom_symbols)
    random.shuffle(all_symbols)
    password = "".join([random.choice(all_symbols) for x in range(length)])
    return password


def shufflePass(password: str) -> str:
    random.shuffle(password)
    return password
