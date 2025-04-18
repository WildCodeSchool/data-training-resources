import discord
from time import sleep

intents = discord.Intents.default()
intents.message_content = True  # Nécessaire pour accéder au contenu des messages

class WildBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'✅ Connecté en tant que {self.user} !')

    async def on_message(self, message):
        try:
            if message.author == self.user:
                return  
            if (
                ((message.guild.name == "WildData" 
                and message.channel.name == "questions-bot-leo") or
                (message.guild.name == "Wild Code School" 
                and message.channel.name == "wild-bot-python"))
                and "?" in message.content
                
            ):
                author = message.author.display_name or message.author.name
                print(f"{author} : {message.content}")
                
                reponse = chat.talk(f"{author} : {message.content}")
                print("Réponse générée :", reponse)
                
                sleep(3)
                await message.channel.send(reponse)
        except Exception:
            pass

