import os
import logging
from dotenv import load_dotenv
from discord import Intents, Client

from responses import generate_flag

# Load environment variables
load_dotenv()  
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

# Set up logging - This is only to ensure there are no errors in-case of unforseen issues
logging.basicConfig(level=logging.INFO)

intents = Intents.default()
intents.messages = True # message perms
intents.dm_messages = True  # bot can DM people
intents.message_content = True  # bot can read messages

client = Client(intents=intents)  

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    logging.info(f'message: {message.content}, Author: {message.author}')
    if message.content.startswith('!flag'):
        flag = generate_flag()
        try:
            await message.author.send(f'`{flag}`')  # Send the flag in a private message
            logging.info(f"Flag sent to {message.author}")
        except Exception as e:
            logging.error(f"Error sending flag: {e}")

if __name__ == '__main__':
    client.run(TOKEN)