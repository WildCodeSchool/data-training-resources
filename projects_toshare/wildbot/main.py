from dotenv import load_dotenv
import os
from gepetto import Gepetto
from bot_discord import WildBot

load_dotenv()

chat = Gepetto(preprompt_key="discord_teacher")
wildbot = WildBot()
wildbot.run(os.getenv("DISCORD_BOT_KEY"))