# This program is to print all the twitch chat messages
# to the console

import os
import json
from dotenv import load_dotenv
from colorist import ColorHex, Effect, BgColor

from twitchio import Message
from twitchio.ext import commands


class ChatOnConsole(commands.Bot):
    def __init__(self, cfg: dict):
        self.cfg = cfg
        super().__init__(token=ACCESS_TOKEN, prefix="", initial_channels=self.cfg.get("CHANNELS", ""))
    
    async def event_ready(self) -> None:
        for channel in self.connected_channels:
            print(f"Connected to : {channel.name}")
    
    async def event_message(self, message: Message) -> None:
        
        if self.cfg.get("SHOW_CHATTER_COLOR"):
            chatter_color: str | None = message.author.color
            
            if chatter_color:
                chatter_color = ColorHex(chatter_color)
            else:
                chatter_color = ColorHex("#FFFFF")
            
            print(f"{chatter_color}{Effect.BOLD}{message.author.name}{Effect.BOLD_OFF}{chatter_color.OFF} : {message.content}")
        
        else:
            # Print without colors (Maybe refactor code to only use one single print)
            pass


def get_config(file: str) -> dict:
    try:
        with open("config.json", "r") as f:
            return json.loads(f.read())
    except Exception as e:
        print(f"Error while reading {file} : {e}")
        exit(-1)


if __name__ == "__main__":

    load_dotenv()
    ACCESS_TOKEN: str = os.getenv("ACCESS_TOKEN")
    # CHANNELS = os.getenv("CHANNELS").split(",")

    obj = ChatOnConsole(get_config("config.json"))
    obj.run()

#TODO: Make this customizable with a json file(Option for timestamps, colors, black and white, notifs or not, etc)
#TODO: Highlight when mentioned
#TODO: Add option to ignore specific user messages(like bots)
#IDEA : Maybe send out a notification everytime a twitch chat is received