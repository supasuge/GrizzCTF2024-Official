import os
from dotenv import load_dotenv
from discord import Intents, Client
import random
import string

# Load environment variables
load_dotenv()  
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

def generate_flag():
    digits_part = ''.join(random.choices(string.digits, k=10))
    chars_part = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"GrizzCTF{{{digits_part}{chars_part}}}"


intents = Intents.default()
intents.messages = True # message perms
intents.dm_messages = True  # bot can DM people
intents.message_content = True  # bot can read messages

client = Client(intents=intents)  

@client.event
async def on_ready():
    print(f"{client.user} has connected to discord successfully")

@client.event
async def on_message(message):
    if message.content.startswith('!flag'):
        flag = generate_flag()
        try:
            await message.author.send(f'`{flag}`')  # Send the flag in a private message
        except Exception as e:
            print(f"Error {e}, {message.author}")

if __name__ == '__main__':
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Error {e}")