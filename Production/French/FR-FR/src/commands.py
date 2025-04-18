# Importation des librairies
import asyncio
import time
from src.logger import print_log
from src.config import config
from src.shellController import shell


# Importation des variables de configuration
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
# Définition des commandes du Bot
#

async def commandHandler(message):    

    if message.content.lower() == pingCommand :
        await message.channel.send('```pong```')
        print_log('INFO', "'Bot' : " + 'pong')



    elif message.content.lower() == helpCommand :
        await message.channel.send( '```' +
                                   'Il existe plusieurs commandes qui sont adressables :\n' + 
                                   '- !' + helpCommand + ' celle que vous venez de taper, elle donne les informations quant aux commandes disponibles.\n' + 
                                   '- !' + ipCommand + " une commande qui donne l'adresse ip du serveur, c'est par là que vous devriez commencer.\n"
                                   '- !' + startServerCommand + ' elle sert évidement à démarrer le serveur, elle nescessite un certain rôle : ' + baseUserRole + '.\n' +
                                   '- !' + restartServerCommand + 'elle sert à redemarrer le serveur, elle est peut être utile en cas de problèmes, elle aussi nescessite un certain rôle : ' + baseUserRole + '.\n'
                                   '- !' + stopServerCommand + " elle sert à arrêter le serveur, elle n'est accessible qu'aux " + adminRole + "les utilisateurs lambdas n'ont pas à l'utiliser car le serveur se met en veille seul.\n" +
                                   '- !' + whitelistCommand + ' elle sert à vous ajouter dans la whitelist du serveur (la liste des utilisateurs autorisés), elle a pour syntaxe : !' + whitelistCommand + ' java/bedrock en fonction de votre support de jeu (java pour la majorité des ordinateurs, bedrock pour les joueurs console si le serveur les supporte) + le pseudo associé.\n' +
                                   'Exemple : !' + whitelistCommand + ' <INSERT_PLATFORM> <INSERT_NAMETAG>'                                    
                                   + '```')
        print_log('INFO', 'La commande Help a été appelée')



    elif message.content.lower() == ipCommand :
        await message.chanel.send('```' + 'Adresse Ip du serveur : ' + serverIp + '```')
        print_log('INFO', "'Bot' : " + '```' + 'Adresse Ip du serveur : ' + serverIp + '```')



    elif message.content.lower() == startServerCommand :
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')

        if baseUserRole in role_names :
            print_log('DEBUG', 'Role autorisé : ' + baseUserRole)

            if shell.is_running():
                await message.channel.send("```Le serveur est déjà actif```")
                shell.send_command('list')
                time.sleep(0.5)
                lines = shell.read_output()
                for line in lines:
                    print_log('INFO', f"Serveur actif - sortie : {line}")

            if not shell.is_running():
                shell.start()
                await message.channel.send('```Commande envoyée, veuillez patienter...```')
                await asyncio.sleep(25)

                if shell.is_running():
                    await message.channel.send('```Le serveur est désormais actif```')
                    print_log('INFO', 'Le serveur est désormais actif')

                if not shell.is_running():
                    await message.channel.send("```Une erreur est survenue, veuillez réessayer, ou contactez l'administrateur")
                    print_log('ERROR', "Une erreur est survenue, veuillez réessayer, ou contactez l'administrateur")
            
        elif not baseUserRole in role_names :
            await message.channel.send("```Vous n'avez pas les droits pour effectuer cette commande```")
            print_log('INFO', message.author + " n'as pas les droits pour effectuer cette commande")



    elif message.content.lower() == restartServerCommand :
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')

        if baseUserRole in role_names :
            print_log('DEBUG', 'Role autorisé : ' + baseUserRole)

            if shell.is_running():
                shell.send_command('restart')
                await message.channel.send('```Commande envoyée, veuillez patienter...```')
                await asyncio.sleep(10)

                if shell.is_running():
                    await message.channel.send("```Le redémarrage a été effectué avec succès```")
                    print_log('INFO', "```Le redémarrage a été effectué avec succès```")

                if not shell.is_running():
                    await message.channel.send("```Une erreur est survenue, veuillez tenter d'ALLUMER le serveur ou contacter l'administrateur```")
                    print_log('ERROR', 'Une erreur est survenue lors du redémarrage')

            elif not shell.is_running():
                await message.channel.send('```Le serveur est déjà éteint```')
                print_log('ERROR', 'Le serveur est déjà éteint')
            
        elif not baseUserRole in role_names :
            await message.channel.send("```Vous n'avez pas les droits pour effectuer cette commande```")
            print_log('INFO', message.author + " n'as pas les droits pour effectuer cette commande")



    elif message.content.lower() == stopServerCommand :
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')

        if adminRole in role_names :
            print_log('DEBUG', 'Role autorisé: ' + adminRole)

            if shell.is_running():
                shell.stop_gracefully()
                await message.channel.send('```Commande envoyée, veuillez patienter...```')
                await asyncio.sleep(10)

                if not shell.is_running():
                    await message.channel.send('```Le serveur est désormais éteint```')
                    print_log('INFO', 'Le serveur est désormais éteint')

                if shell.is_running():
                    await message.channel.send("```Une erreur est survenue, veuillez tenter d'ALLUMER le serveur ou contacter l'administrateur")
                    print_log('ERROR', "Une erreur est survenue, veuillez tenter d'ALLUMER le serveur ou contacter l'administrateur```")
                
            elif not shell.is_running():
                await message.channel.send('```Le serveur est déjà éteint```')
                print_log('INFO', 'Le serveur est déjà éteint')
            
        elif not adminRole in role_names :
            await message.channel.send("```Vous n'avez pas les droits pour effectuer cette commande```")
            print_log('INFO', message.author + " n'as pas les droits pour effectuer cette commande")



    elif whitelistCommand in message.content.lower() :
        message.content = message.content[len(whitelistCommand) + 1:]
        role_names = [role.name for role in message.author.roles]
        print_log('DEBUG', f'User roles: {role_names}')
            
        if baseUserRole in role_names :
            print_log('DEBUG', 'Role autorisé: ' + baseUserRole)

            if 'java' in message.content.lower() :
                message.content = message.content[4+1:]

                if shell.is_running():
                    shell.send_command('whitelist add ' + message.content)
                    await message.channel.send('```Commande envoyée, veuillez patienter...```')
                    await asyncio.sleep(1)
                    lines = shell.read_output()
                    for line in lines:
                        print_log('INFO', f"Serveur actif - sortie : {line}")

                    if any('Added' in line for line in lines):
                        await message.channel.send('```Joueur ajouté à la whitelist```')
                        print_log('INFO', 'Joueur ajouté à la whitelist par ' + message.author)
                        
                    elif any('alredy' in line for line in lines):
                         await message.channel.send('```Joueur déjà présent dans la whitelist```')
                         print_log('INFO', 'Joueur déjà présent dans la whitelist')
                        
                    else:
                         await message.channel.send("```Erreur lors de l'ajout du joueur```")
                         print_log('ERROR', "Erreur lors de l'ajout du joueur")

                if not shell.is_running():
                    await message.channel.send("```Le serveur est éteint, impossible d'ajouter un joueur, essayez de l'allumer en utilisant la commande '!" + startServerCommand + "'```")
                    print_log('INFO', "Le serveur est éteint, impossible d'ajouter un joueur")

            if 'bedrock' in message.content.lower() :
                message.content = message.content[7+1:]

                if shell.is_running():
                    shell.send_command('fwhitelist add ' + message.content)
                    await message.channel.send('```Commande envoyée, veuillez patienter...```')
                    await asyncio.sleep(1)
                    lines = shell.read_output()
                    for line in lines:
                        print_log('INFO', f"Serveur actif - sortie : {line}")

                    if any('Added' in line for line in lines):
                        await message.channel.send('```Joueur ajouté à la whitelist```')
                        print_log('INFO', 'Joueur ajouté à la whitelist par ' + message.author)
                        
                    elif any('already' in line for line in lines):
                        await message.channel.send('```Joueur déjà présent dans la whitelist```')
                        print_log('INFO', 'Joueur déjà présent dans la whitelist')
                        
                    else:
                         await message.channel.send("```Erreur lors de l'ajout du joueur```")
                         print_log('ERROR', "Erreur lors de l'ajout du joueur")

                if not shell.is_running():
                    await message.channel.send("```Le serveur est éteint, impossible d'ajouter un joueur, please try to start the server with the command : '!" + startServerCommand + "'```")
                    print_log('INFO', "Le serveur est éteint, impossible d'ajouter un joueur")
            
        elif not baseUserRole in role_names :
            await message.channel.send("```Vous n'avez pas les droits pour effectuer cette commande```")
            print_log('INFO', message.author + " n'as pas les droits pour effectuer cette commande")
   