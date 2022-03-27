import logging

LOGGER = logging.getLogger('discord')
LOGGER.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
LOGGER.addHandler(handler)

TOKEN = "OTQ1MTI0MzExMDg0MTgzNTcz.YhLlmw.P2kEwJJNocflaXrFNnOMz4TNxA4"