import asyncio, time
import requests as r
import os
from keep_alive import keep_alive
import websocket
import colorama
from colorama import Fore, init
import requests
import random
import time

token = os.getenv("token")
channel_id = os.getenv("channel_id")
messages = ['yo', 'true', 'real', 'nah', 'wsg', 'hy', 'ok', 'ye', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'fs', 'fs bro', '7', 'yea gng', 'shut up', '?', 'ugly asl', 'nigga what', 'nigga', 'bro lmaooo', 'where the opps? awl shit', 'the pigeon it yesterday', 'cuck ass nikka', 'im bored', 'im bored asl', 'tired', 'im sleepy', 'tired asf', 'horny asl', 'horny miss that eseggs', 'clown', 'yo what', 'ignored', 'ii', 'no', 'finna flame shit up wit twin', 'high asl', 'x', 'les play some who got games', 'who got', 'chat dry asf', 'it', 'u', 'big 2025', 'no', 'ikr', 'let it shine', 'huh', 'jvc', 'furrys rule the world', 'are you a furry?', 'yo wassup bro', 'nigga stfu', 'igh bro', 'wtf you talking about', 'yap', 'osamason', 'jely', 'good cumslut goood', 'u got a 6 head', 'no dad no mom?', 'gah dam', 'you look good twin', 'love my cats', 'im back', 'nigga what the fuck', 'no arc', 'built like a anglerfish', 'you are a loner', 'bro no stop it', 'stop touching me pls', 'love me a lover girl', 'oh my god we dont care', 'stupid', 'dickhead', 'idiot', 'clown', 'yappatron', 'yapping is all you do', 'im here', 'ay im active', 'bum', 'me and my guitar', 'skid', 'loner', 'black', 'hahahaha', 'LOL', 'XD', 'LMAO', 'LO', 'OL', 'LOOOL','LMAO', 'stfu LMAO', 'awl shit', 'wow', 'loser', 'random', 'what de fuc?', 'myf', 'bruh', 'what', 'how?', 'cool', 'na', 'precummin', 'Bro is a walking DLC with extra lives.', 'nigga', 'bro what the fuck', 'Bro is a walking medkit', 'hi', 'als goat here', 'niga ass', 'funny ass dude bro', 'bros a side quest', 'bro angry', 'corny nigga', 'ty', 'o', 'horny', 'are you a good slut?', 'good bitch', 'kiwi & arthur my goats', 'im up', 'poor ass fag clown', 'diee', 'money love money', 'never stoppin nigga im thuggin', '?', 'stop talking', 'nigga', 'harassin a nigga', 'chigga', 'im too sexy', 'shove a nuke up yo pussy', 'hi im monty', '@////@', ';-;', 'good', 'nigga', 'idk twin', '(:', 'c:', ':c', '>:c', 'c:<', '>:(', '(:<', '>;)', '(;<', '>;c', 'ek', 'UwU', 'T-T', 'fin crash', 'over and over ill fall for you', 'you seggsy hm?']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
}

userinfo = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

print(f'''
{Fore.RED}╦╔═╦ ╦╔═╗╦ ╦╔╦╗╔═╗
{Fore.RED}╠╩╗╚╦╝╠═╣║ ║ ║ ║ ║
{Fore.RED}╩ ╩ ╩ ╩ ╩╚═╝ ╩ ╚═╝
{Fore.RESET}-----------------------
{Fore.RESET}USER INFO:
{Fore.GREEN}User: @{username}
{Fore.YELLOW}ID: {userid}
{Fore.BLUE}Channel: {channel_id}
''')

while True:
    wait_time = random.randint(1, 2)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'{Fore.RESET}[@{Fore.YELLOW}KYAUTO{Fore.RESET}] [Waiting {Fore.RED}{str(wait_time)} seconds...{Fore.RESET}] {Fore.GREEN}Sent message {Fore.RESET}> {Fore.MAGENTA}{message}{Fore.RESET}')
    keep_alive()
    time.sleep(wait_time)
