import discord
import requests
import subprocess
import os
import random

# TODO Features:
# Start aws instance-requires separate instance and full aws version
# Print console output?

client = discord.Client()
key = open('key.txt').readline()

csBool = False
gsBool = False
lsBool = False

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!abhelp') or message.content.startswith('!help'):
        await message.channel.send('!abhelp, !abip, !abstatus, ![start/stop/restart][LS/CS/GS/All].')
    if message.content.startswith('!abip'):
        r = requests.get('https://api.ipify.org/?format=json')
        await message.channel.send(r.json())
    if message.content.startswith('!abstatus') or message.content.startswith('!stat'):
        await message.channel.send("CS:" + str(csBool) + " GS:" + str(gsBool) + " LS:" + str(lsBool))
    if message.content.startswith('!startAll') or message.content.startswith('!on'):
        await startLS(message)
        await startCS(message)
        await startGS(message)
    if message.content.startswith('!stopAll') or message.content.startswith('!off'):
        await stopLS(message)
        await stopCS(message)
        await stopGS(message)
    if message.content.startswith('!restartAll') or message.content.startswith('!res'):
        await stopLS(message)
        await stopCS(message)
        await stopGS(message)
        await startLS(message)
        await startCS(message)
        await startGS(message)
    if message.content.startswith('!startLS'):
        await startLS(message)
    if message.content.count('!stopLS'):
        await stopLS(message)
    if message.content.startswith('!startCS'):
        await startCS(message)
    if message.content.count('!stopCS'):
        await stopCS(message)
    if message.content.startswith('!startGS'):
        await startGS(message)
    if message.content.count('!stopGS'):
        await stopGS(message)

async def startLS(message):
    global lsBool, lsProc
    if not lsBool:
        await message.channel.send('Starting LS.')
        os.chdir('C:\\Users\\Administrator\\Desktop\\Aion-Core-v4.7.5-master\\AC-Login\\build\\dist\\AC-Login')
        lsProc = subprocess.Popen('JAVA -version:"1.7" -XX:-UseSplitVerifier -Xms64m -Xmx64m -server -cp ./libs/*;ac-login.jar com.aionemu.loginserver.LoginServer', creationflags=subprocess.CREATE_NEW_CONSOLE)
        lsBool = True
    else:
        await message.channel.send('LS already running.')
async def stopLS(message):
    global lsBool
    if lsBool:
        await message.channel.send('Closing LS.')
        lsProc.kill()
        lsBool = False
    else:
        await message.channel.send('LS is already stopped.')
async def startCS(message):
    global csBool, csProc
    if not csBool:
        await message.channel.send('Starting CS.')
        os.chdir('C:\\Users\\Administrator\\Desktop\\Aion-Core-v4.7.5-master\\AC-Chat\\build\\dist\\AC-Chat')
        csProc = subprocess.Popen('JAVA -version:"1.7" -XX:-UseSplitVerifier -Xms64m -Xmx64m -server -cp ./libs/*;ac-chat.jar com.aionemu.chatserver.ChatServer', creationflags=subprocess.CREATE_NEW_CONSOLE)
        csBool = True
    else:
        await message.channel.send('CS already running.')
async def stopCS(message):
    global csBool
    if csBool:
        await message.channel.send('Closing CS.')
        csProc.kill()
        csBool = False
    else:
        await message.channel.send('CS is already stopped.')
async def startGS(message):
    global gsBool,gsProc
    if not gsBool:
        await message.channel.send('Starting GS.')
        os.chdir('C:\\Users\\Administrator\\Desktop\\Aion-Core-v4.7.5-master\\AC-Game\\build\\dist\\AC-Game')
        gsProc = subprocess.Popen('JAVA -version:"1.7" -XX:-UseSplitVerifier -Xms3872m -Xmx3872m -server -ea -javaagent:./libs/ac-commons-1.3.jar -cp ./libs/*;AC-Game.jar com.aionemu.gameserver.GameServer', creationflags=subprocess.CREATE_NEW_CONSOLE)
        gsBool = True
    else:
        await message.channel.send('GS already running.')
async def stopGS(message):
    global gsBool
    if gsBool:
        await message.channel.send('Closing GS.')
        gsProc.kill()
        gsBool = False
    else:
        await message.channel.send('GS is already stopped.')

client.run(key)