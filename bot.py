import discord
import requests
from discord.ext import commands
import pyttsx3   
import random  
import translate
from translate import Translator  
def traducir(text):
    traductor = Translator(to_lang="es", from_lang="en")
    traduccion=traductor.translate(text)
    return traduccion



# Función para que el compu hable
def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)   
    engine.setProperty('volume', 1.0) 
    voices = engine.getProperty('voices')   
    engine.setProperty('voice', voices[0].id)  
    engine.say(text)     
    engine.runAndWait()  

intents=discord.Intents.default()
intents.message_content = True


bot=commands.Bot(command_prefix="$",intents=intents)


@bot.command()
async def hola(ctx):
    await ctx.send("Hola soy tu asistente virtual")

#api #1
def obtener_clima(ciudad : str) -> str:
    url= f"https://wttr.in/{ciudad}?format=%C+%t&lang=es"
    respuesta=requests.get(url)

    if respuesta.status_code == 200:
        return respuesta.text.strip()
    else:
        return "Error no se pudo obtener la informacion de la API"
    
#api #2
def fun_facts() -> str:
    url= f"https://uselessfacts.jsph.pl/random.json"
    respuesta=requests.get(url)

    if respuesta.status_code == 200:
        return respuesta.json().get("text","No se pudo obtener este dato")
    else:
        return "Error no se pudo conectar a la API"
 
        
   

#Comando #2
@bot.command()
async def clima(ctx, *,ciudad:str):
    prediccion=obtener_clima(ciudad)
    await ctx.send(f"El clima en {ciudad} es:{prediccion}")
    talk(f"El clima en {ciudad} es:{prediccion}")

@bot.command()
async def fact(ctx):
    facto=fun_facts()
    facto=traducir(facto)
    await ctx.send(f"Tu dato curioso es: {facto}")
    talk(f"Tu dato curioso es: {facto}")




bot.run(TOKEN)
