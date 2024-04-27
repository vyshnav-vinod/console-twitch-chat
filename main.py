# This program is to print all the twitch chat messages
# to the console

import os
from dotenv import load_dotenv

from twitchio import Message
from twitchio.ext import commands

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
CHANNELS = os.getenv("CHANNELS").split(",")

class ChatOnConsole(commands.Bot):
    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix="", initial_channels=CHANNELS)
    
    async def event_ready(self) -> None:
        for channel in self.connected_channels:
            print(f"Connected to : {channel.name}")
    
    async def event_message(self, message: Message) -> None:
        print(f"{message.author.name}: {message.content}")


if __name__ == "__main__":
    obj = ChatOnConsole()
    obj.run()

#IDEA : Maybe send out a notification everytime a twitch chat is received