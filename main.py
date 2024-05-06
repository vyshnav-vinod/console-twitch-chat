# This program is to print all the twitch chat messages
# to the console

import os
import json
import datetime
from dotenv import load_dotenv
from colorist import ColorHex, Effect

from twitchio import Message
from twitchio.ext import commands


class ChatOnConsole(commands.Bot):
    def __init__(self, cfg: dict) -> None:
        try:
            self.cfg: dict = cfg
            super().__init__(token=ACCESS_TOKEN, prefix="", initial_channels=self.cfg.get("CHANNELS", ""))
        except Exception as e:
            handle_error(e)
            
    async def event_ready(self) -> None:
        for channel in self.connected_channels:
            print(f"Connected to : {channel.name}")
    
    async def event_message(self, message: Message) -> None:
        result_chat: dict = {}
        result_chat["chatter"] = message.author.name
        result_chat["content"] = message.content    
        channel_name = message.channel.name
        result_chat["mention"] = True if not result_chat["content"].lower().find(channel_name.lower()) == -1 else False

        if self.cfg.get("SHOW_CHATTER_COLOR"):
            chatter_color: str | None = message.author.color
            chatter_color = ColorHex(chatter_color) if chatter_color else ColorHex("#FFFFFF")
            result_chat["color"] = chatter_color
            timestamp = message.timestamp if self.cfg.get("SHOW_TIMESTAMP") else ""
        
        else:
            result_chat["color"] = ColorHex("#FFFFFF")
            timestamp = message.timestamp if self.cfg.get("SHOW_TIMESTAMP") else ""

        result_chat["timestamp"] = timestamp
        print_chat(result_chat)


def get_config(file: str) -> dict:
    try:
        with open("cfg.json", "r") as f:
            return json.loads(f.read())
    except Exception as e:
        print(f"Error while reading {file} : {e}")
        exit(-1)


def print_chat(result_chat: dict) -> None:
    timestamp:datetime.datetime | None = ""
    color: ColorHex = result_chat["color"]
    chatter: str = result_chat["chatter"]
    message: str = result_chat["content"]
    mention: bool = result_chat["mention"]

    if result_chat["timestamp"]:
        timestamp = result_chat["timestamp"].time().strftime("%H:%M") # It is in UTC
        if not mention:
            print(f"{Effect.BOLD}{color}{chatter} [{timestamp}]{color.OFF}{Effect.BOLD_OFF}{Effect.OFF}: {message}")
        else:
            print(f"{Effect.UNDERLINE}{Effect.BOLD}{color}{chatter} [{timestamp}]{color.OFF}{Effect.OFF}{Effect.UNDERLINE}: {message}{Effect.UNDERLINE_OFF}{Effect.OFF}")
    
    else:
        if not mention:
            print(f"{Effect.BOLD}{color}{chatter}{color.OFF}{Effect.BOLD_OFF}{Effect.OFF}: {message}")
        else:
            print(f"{Effect.UNDERLINE}{Effect.BOLD}{color}{chatter}{color.OFF}{Effect.OFF}{Effect.UNDERLINE}: {message}{Effect.UNDERLINE_OFF}{Effect.OFF}")


def handle_error(e: Exception):
    print("Encountered an error : {e}")
    exit(-1)


if __name__ == "__main__":
    load_dotenv()
    ACCESS_TOKEN: str = os.getenv("ACCESS_TOKEN")

    try:
        obj = ChatOnConsole(get_config("config.json"))
        obj.run()
    except Exception as e:
        handle_error(e)

#TODO: Add option to ignore specific user messages(like bots)
#TODO: Add specific symbols or colors to display whether the user is a mod, broadcaster or the vip
#IDEA : Maybe send out a notification everytime a twitch chat is received
#IDEA: A complete clone of the twitch chat, with popups ,first time chat alert, colors, etc (Look into TUI libs)
