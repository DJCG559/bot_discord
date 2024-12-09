import discord
import os
from dotenv import load_dotenv
from juegos import gen_juego
from psw import gen_pass
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

#textos de bot en discord s    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('*hola'):
        await message.channel.send("hola")
    
    elif message.content.startswith('*como estas'):
        await message.channel.send("bien y tu")

    elif message.content.startswith('*barca o Madrid'):
        await message.channel.send("Madrid es mejor que barca!!")

    elif message.content.startswith('*adios'):
        await message.channel.send("adios")

    elif message.content.startswith('*psw'):
         await message.channel.send("Aqui tienes la contrasena:" + gen_pass(8))

    elif message.content.startswith("*juego"):
         await message.channel.send("Aqui tienes un juego:" + gen_juego())

    else:
         await message.channel.send(message.content)

token = os.getenv('DISCORD_BOT_TOKEN')

client.run(token)
 




