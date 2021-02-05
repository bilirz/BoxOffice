import random


def deleteSpace(list):
    return [l for l in list if l != ""]


def randomAgent():
    with open("./data/spider/User-Agent.txt", "r", encoding="utf-8-sig") as f:
        userAgents = f.read().split("\n")
    return random.choice(deleteSpace(userAgents))
