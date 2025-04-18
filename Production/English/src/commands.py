# Libraries importation
import asyncio
import time
from src.logger import print_log
from src.config import config
from src.shellController import shell


# Importation of configuration variables
baseUserRole = config['baseUserRole']
adminRole = config['adminRole']
serverIp = config['serverIp']
pingCommand = config['pingCommand']
helpCommand = config['helpCommand']
ipCommand = config['ipServerCommand']
startServerCommand = config['startServerCommand']
restartServerCommand = config['restartServerCommand']
stopServerCommand = config['stopServerCommand']
whitelistCommand = config['whitelistCommand']

#
# Definition of the Bot commands
#

async def commandHandler(message):    

    if message.content.lower() == pingCommand :
        await message.channel.send('```pong```')
        print_log('INFO', "'Bot' : " + 'pong')



    elif message.content.lower() == helpCommand :
        await message.channel.send(
                                    '```' +
                                    'There are several available commands:\n' +
                                    '- !' + helpCommand + ' — the one you just used; it shows information about available commands.\n' +
                                    '- !' + ipCommand + " — provides the IP address of the server, which is where you should start.\n" +
                                    '- !' + startServerCommand + ' — starts the server; requires a specific role: ' + baseUserRole + '.\n' +
                                    '- !' + restartServerCommand + ' — restarts the server, useful in case of issues; also requires the role: ' + baseUserRole + '.\n' +
                                    '- !' + stopServerCommand + ' — stops the server; only accessible to ' + adminRole + '; regular users don’t need it as the server shuts down automatically.\n' +
                                    '- !' + whitelistCommand + ' — adds you to the server whitelist (authorized player list); usage: !' + whitelistCommand + ' java/bedrock depending on your platform (java for most PC players, bedrock for consoles if supported) followed by your username.\n' +
                                    'Example: !' + whitelistCommand + ' <INSERT_PLATFORM> <INSERT_NAMETAG>' +
                                    '```')
        print_log('INFO', 'Help command have been used')



    elif message.content.lower() == ipCommand :
        await message.chanel.send('```' + 'Server Ip adress : ' + serverIp + '```')
        print_log('INFO', "'Bot' : " + '```' + 'Server Ip adress : ' + serverIp + '```')



    elif message.content.lower() == startServerCommand :
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')

        if baseUserRole in role_names :
            print_log('DEBUG', 'right role: ' + baseUserRole)

            if shell.is_running():
                await message.channel.send("```Server already online```")
                shell.send_command('list')
                time.sleep(0.5)
                lines = shell.read_output()
                for line in lines:
                    print_log('INFO', f"Serveur online - output : {line}")

            if not shell.is_running():
                shell.start()
                await message.channel.send('```Command sent, please wait...```')
                await asyncio.sleep(25)

                if shell.is_running():
                    await message.channel.send('```The server now online```')
                    print_log('INFO', 'The server now online')

                if not shell.is_running():
                    await message.channel.send("```An error happened, please retry, or contact the administrator")
                    print_log('ERROR', "An error happened, please retry, or contact the administrator")
            
        elif not baseUserRole in role_names :
            await message.channel.send("```You have not the right to send this command```")
            print_log('INFO', message.author + " has not the right to send this command")



    elif message.content.lower() == restartServerCommand :
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')

        if baseUserRole in role_names :
            print_log('DEBUG', 'right role: ' + baseUserRole)

            if shell.is_running():
                shell.send_command('restart')
                await message.channel.send('```Command sent, please wait...```')
                await asyncio.sleep(10)

                if shell.is_running():
                    await message.channel.send("```The server successfuly restart```")
                    print_log('INFO', "```The server successfuly restart```")

                if not shell.is_running():
                    await message.channel.send("```An error happened, please try to start the server or contact the administrator```")
                    print_log('ERROR', 'An error happened when restarting')

            elif not shell.is_running():
                await message.channel.send('```The server already offline```')
                print_log('ERROR', 'The server already offline')
            
        elif not baseUserRole in role_names :
            await message.channel.send("```You have not the right to send this command```")
            print_log('INFO', message.author + " has not the right to send this command")



    elif message.content.lower() == stopServerCommand :
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')

        if adminRole in role_names :
            print_log('DEBUG', 'right role: ' + adminRole)

            if shell.is_running():
                shell.stop_gracefully()
                await message.channel.send('```Command sent, please wait...```')
                await asyncio.sleep(10)

                if not shell.is_running():
                    await message.channel.send('```The server now offline```')
                    print_log('INFO', 'The server now offline')

                if shell.is_running():
                    await message.channel.send("```An error happened, please try to start the server or contact the administrator")
                    print_log('ERROR', "An error happened, please try to start the server or contact the administrator```")
                
            elif not shell.is_running():
                await message.channel.send('```The server already offline```')
                print_log('INFO', 'The server already offline')
            
        elif not adminRole in role_names :
            await message.channel.send("```You have not the right to send this command```")
            print_log('INFO', message.author + " has not the right to send this command")



    elif whitelistCommand in message.content.lower() :
        message.content = message.content[len(whitelistCommand) + 1:]
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')
            
        if baseUserRole in role_names :
            print_log('DEBUG', 'right role: ' + baseUserRole)

            if 'java' in message.content.lower() :
                message.content = message.content[4+1:]

                if shell.is_running():
                    shell.send_command('whitelist add ' + message.content)
                    await message.channel.send('```Command sent, please wait...```')
                    await asyncio.sleep(1)
                    lines = shell.read_output()
                    for line in lines:
                        print_log('INFO', f"Server online - output : {line}")

                    if any('Added' in line for line in lines):
                        await message.channel.send('```Player added to the whitelist```')
                        print_log('INFO', 'Player added to the whitelist by ' + message.author)
                        
                    elif any('alredy' in line for line in lines):
                         await message.channel.send('```Player already in the whitelist```')
                         print_log('INFO', 'Player already in the whitelist')
                        
                    else:
                         await message.channel.send("```An error occurred while adding the player```")
                         print_log('ERROR', "An error occurred while adding the player")

                if not shell.is_running():
                    await message.channel.send("```The server offline, impossible adding a player, please try to start the server with the command : '!'" + startServerCommand + "```")
                    print_log('INFO', "The server offline, impossible adding a player")

            if 'bedrock' in message.content.lower() :
                message.content = message.content[7+1:]

                if shell.is_running():
                    shell.send_command('fwhitelist add ' + message.content)
                    await message.channel.send('```Command sent, please wait...```')
                    await asyncio.sleep(1)
                    lines = shell.read_output()
                    for line in lines:
                        print_log('INFO', f"Server online - output : {line}")

                    if any('Added' in line for line in lines):
                        await message.channel.send('```Player added to the whitelist```')
                        print_log('INFO', 'Player added to the whitelist by ' + message.author)
                        
                    elif any('already' in line for line in lines):
                        await message.channel.send('```Player already in the whitelist```')
                        print_log('INFO', 'Player already in the whitelist')
                        
                    else:
                         await message.channel.send("```An error occurred while adding the player```")
                         print_log('ERROR', "An error occurred while adding the player")

                if not shell.is_running():
                    await message.channel.send("```The server offline, impossible adding a player, please try to start the server with the command : '!" + startServerCommand + "'```")
                    print_log('INFO', "The server offline, impossible adding a player")
            
        elif not baseUserRole in role_names :
            await message.channel.send("```You have not the right to send this command```")
            print_log('INFO', message.author + " has not the right to send this command")
   