# This program is to print all the twitch chat messages
# to the console

import os
from dotenv import load_dotenv
from colorist import ColorHex, Effect

from twitchio import Message
from twitchio.ext import commands


class ChatOnConsole(commands.Bot):
    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix="", initial_channels=CHANNELS)
    
    async def event_ready(self) -> None:
        for channel in self.connected_channels:
            print(f"Connected to : {channel.name}")
    
    async def event_message(self, message: Message) -> None:
        chatter_color = message.author.color
        
        if chatter_color:
            chatter_color = ColorHex(chatter_color)
        else:
            chatter_color = ColorHex("#FFFFF")
        
        print(f"{chatter_color}{Effect.BOLD}{message.author.name}{Effect.BOLD_OFF}{chatter_color.OFF} : {message.content}")


if __name__ == "__main__":

    load_dotenv()
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    CHANNELS = os.getenv("CHANNELS").split(",")

    obj = ChatOnConsole()
    obj.run()

#TODO: Make this customizable with a json file(Option for timestamps, colors, black and white, notifs or not, etc)
#TODO: Add option to ignore specific user messages(like bots)
#IDEA : Maybe send out a notification everytime a twitch chat is received