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
messages = ['yo', 'true', 'real', 'nah', 'wsg', 'hy', 'ok', 'ye', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'fs', 'fs bro', '7', 'who tryna vc', 'shut up', 'f4f?', 'ugly asl', 'nigga what', 'nigga', 'brother', 'where the opps', 'when you see me dont blink', 'cuck', 'im bored', 'im bored asl', 'tired', 'im sleepy', 'tired asf', 'horny asl', 'horny', 'clown', 'yo what', 'ignored', 'test', 'no', 'finna flame', 'high asl', 'who got roblox?', 'who got fort?', 'who got', 'eating', 'it', 'u', 'big 2025', 'no', 'ikr', 'sunshine lollipops and rainbows', 'whats in your wallet', 'jvc', 'ur a furry', 'yo wassup bro', 'nigga stfu', 'igh bro', 'wtf you talking about', 'yap', 'sing ason', 'jely', 'good cumslut', 'u got 8 fingers', 'wheres your dad?', 'gah dam', 'you look good twin', 'love my cats', 'im back', 'nigga what the fuck', 'you have no arc', 'no arc', 'you are a loner', 'bro no stop it', 'stop touching me pls', 'oh my god we dont care', 'stupid', 'dickhead', 'idiot', 'clown', 'yappatron', 'stop yapping', 'im here', 'get more active', 'bum', 'no dogecoin', 'dskid', 'loner', 'black', 'hahahaha', 'LOL', 'XD', 'LMAO', 'LO', 'OL', 'LOOOLOLOOLL','LMAOOOOOOOOO', 'stfu LMAO', 'ah shucks', 'wow', 'loser', 'random', 'what the hell?', 'talking nonsense', 'bruh', 'what', 'how?', 'cool', 'show a band', 'pooron', 'trash', 'nigga', 'bro what', 'dude is a health pack', 'hi', 'als goat here', 'niga ass', 'you funny asf', 'bros not the mc', 'bro mad', 'cornball', 'ty', 'o', 'horny', 'are you a good slut', 'im rich', 'ur poor', 'come die', 'money love money', 'never stop', '????', 'stop talking', 'nigga', 'harassment', 'im a comboy', 'im too sexy','shove a nuke up yo pussy', 'hi im monty :p', ':/', ':)', ':(', ';(', '):', '(:', 'c:', ':c', '>:c', 'c:<', '>:(', '(:<', '>;)', '(;<', '>;c', 'ek', 'UwU', 'T-T', 'crashout', 'over and over ill fall for you', 'you seggsy?']
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
    wait_time = random.randint(10, 12)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'{Fore.RESET}[@{Fore.YELLOW}KYAUTO{Fore.RESET}] [Waiting {Fore.RED}{str(wait_time)} seconds...{Fore.RESET}] {Fore.GREEN}Sent message {Fore.RESET}> {Fore.MAGENTA}{message}{Fore.RESET}')
    keep_alive()
    time.sleep(wait_time)
