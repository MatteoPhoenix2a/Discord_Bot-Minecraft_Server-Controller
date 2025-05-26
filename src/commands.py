# Libraries importation
import asyncio
import time
from src.logger import print_log
from src.config import config
from src.config import language_config
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

# Importation of the language
helpIntroduction = language_config['helpCommandResponse'][0]['introduction']
helpDescription = language_config['helpCommandResponse'][0]['helpCommandDescription']
ipDescription = language_config['helpCommandResponse'][0]['ipCommandDescription']
startServerDescription = language_config['helpCommandResponse'][0]['startServerCommandDescription']
restartServerDescription = language_config['helpCommandResponse'][0]['restartServerCommandDescription']
stopServerDescription = language_config['helpCommandResponse'][0]['stopServerCommandDescription']
whitelistDescription = language_config['helpCommandResponse'][0]['whitelistCommandDescription']
whitelistExample = language_config['helpCommandResponse'][0]['whitelistCommandExample']

baseError = language_config['classicOutputs'][0]['errors'][0]['error']
roleError = language_config['classicOutputs'][0]['errors'][0]['roleError']
serverOnlineError = language_config['classicOutputs'][0]['errors'][0]['serverOnlineError']
serverOfflineError = language_config['classicOutputs'][0]['errors'][0]['serverOfflineError']
whitelistError = language_config['classicOutputs'][0]['errors'][0]['whitelistCommandError'][0]['whitelistError']
playerAlreadyAdded = language_config['classicOutputs'][0]['errors'][0]['whitelistCommandError'][0]['playerAlreadyAdded']
whitelistOfflineError = language_config['classicOutputs'][0]['errors'][0]['whitelistCommandError'][0]['whitelistOfflineError']

whitelistSuccess = language_config['classicOutputs'][0]['successes'][0]['whitelistCommandSuccess']
startServerSuccess = language_config['classicOutputs'][0]['successes'][0]['startServerCommandSuccess']
restartServerSuccess = language_config['classicOutputs'][0]['successes'][0]['restartServerCommandSuccess']
stopServerSuccess = language_config['classicOutputs'][0]['successes'][0]['stopServerCommandSuccess']

commandSent = language_config['classicOutputs'][0]['miscellaneous'][0]['commandSent']


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
                                    helpIntroduction + '\n' +
                                    '- !' + helpCommand + helpDescription + '\n' +                  
                                    '- !' + ipCommand + ipDescription + '\n' +
                                    '- !' + startServerCommand + startServerDescription + baseUserRole + '\n' +
                                    '- !' + restartServerCommand + restartServerDescription + baseUserRole + '\n' +
                                    '- !' + stopServerCommand + stopServerDescription + adminRole + '\n' +
                                    '- !' + whitelistCommand + whitelistDescription + '\n' +
                                    whitelistExample +
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
                await message.channel.send("```" + serverOnlineError + "```")
                shell.send_command('list')
                time.sleep(0.5)
                lines = shell.read_output()
                for line in lines:
                    print_log('INFO', f"Serveur online - output : {line}")

            if not shell.is_running():
                shell.start()
                await message.channel.send('```' + commandSent + '```')
                await asyncio.sleep(25)

                if shell.is_running():
                    await message.channel.send('```' + startServerSuccess + '```')
                    print_log('INFO', 'The server now online')

                if not shell.is_running():
                    await message.channel.send('```' + baseError + '```')
                    print_log('ERROR', "An error happened, please retry, or contact the administrator")
            
        elif not baseUserRole in role_names :
            await message.channel.send('```' + roleError+ '```')
            print_log('INFO', message.author + " has not the right to send this command")



    elif message.content.lower() == restartServerCommand :
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')

        if baseUserRole in role_names :
            print_log('DEBUG', 'right role: ' + baseUserRole)

            if shell.is_running():
                shell.send_command('restart')
                await message.channel.send('```' + commandSent + '```')
                await asyncio.sleep(10)

                if shell.is_running():
                    await message.channel.send("```" + restartServerSuccess + "```")
                    print_log('INFO', "```The server successfuly restart```")

                if not shell.is_running():
                    await message.channel.send('```' + baseError + '```')
                    print_log('ERROR', 'An error happened when restarting')

            elif not shell.is_running():
                await message.channel.send('```' + serverOfflineError + '```')
                print_log('ERROR', 'The server already offline')
            
        elif not baseUserRole in role_names :
            await message.channel.send('```' + roleError+ '```')
            print_log('INFO', message.author + " has not the right to send this command")



    elif message.content.lower() == stopServerCommand :
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')

        if adminRole in role_names :
            print_log('DEBUG', 'right role: ' + adminRole)

            if shell.is_running():
                shell.stop_gracefully()
                await message.channel.send('```' + commandSent + '```')
                await asyncio.sleep(10)

                if not shell.is_running():
                    await message.channel.send('```' + stopServerSuccess + '```')
                    print_log('INFO', 'The server now offline')

                if shell.is_running():
                    await message.channel.send('```' + baseError+ '```')
                    print_log('ERROR', "An error happened, please try to start the server or contact the administrator```")
                
            elif not shell.is_running():
                await message.channel.send('```' + serverOfflineError + '```')
                print_log('INFO', 'The server already offline')
            
        elif not adminRole in role_names :
            await message.channel.send('```' + roleError+ '```')
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
                    await message.channel.send('```' + commandSent + '```')
                    await asyncio.sleep(1)
                    lines = shell.read_output()
                    for line in lines:
                        print_log('INFO', f"Server online - output : {line}")

                    if any('Added' in line for line in lines):
                        await message.channel.send('```' + whitelistSuccess + '```')
                        print_log('INFO', 'Player added to the whitelist by ' + message.author)
                        
                    elif any('alredy' in line for line in lines):
                         await message.channel.send('```' + playerAlreadyAdded + '```')
                         print_log('INFO', 'Player already in the whitelist')
                        
                    else:
                         await message.channel.send('```' + whitelistError+ '```')
                         print_log('ERROR', "An error occurred while adding the player")

                if not shell.is_running():
                    await message.channel.send('```' + whitelistOfflineError + startServerCommand +  '```')
                    print_log('INFO', "The server offline, impossible adding a player")

            if 'bedrock' in message.content.lower() :
                message.content = message.content[7+1:]

                if shell.is_running():
                    shell.send_command('fwhitelist add ' + message.content)
                    await message.channel.send('```' + commandSent + '```')
                    await asyncio.sleep(1)
                    lines = shell.read_output()
                    for line in lines:
                        print_log('INFO', f"Server online - output : {line}")

                    if any('Added' in line for line in lines):
                        await message.channel.send('```' + whitelistSuccess + '```')
                        print_log('INFO', 'Player added to the whitelist by ' + message.author)
                        
                    elif any('already' in line for line in lines):
                        await message.channel.send('```' + playerAlreadyAdded + '```')
                        print_log('INFO', 'Player already in the whitelist')
                        
                    else:
                         await message.channel.send('```' + whitelistError+ '```')
                         print_log('ERROR', "An error occurred while adding the player")

                if not shell.is_running():
                    await message.channel.send('```' + whitelistOfflineError + startServerCommand +  '```')
                    print_log('INFO', "The server offline, impossible adding a player")
            
        elif not baseUserRole in role_names :
            await message.channel.send('```' + roleError+ '```')
            print_log('INFO', message.author + " has not the right to send this command")
   