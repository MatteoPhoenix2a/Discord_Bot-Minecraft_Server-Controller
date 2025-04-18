# Importation des librairies
import time
from src.shellController import shell
from src.config import config
from src.logger import print_log
from src.bot import client
import re
import discord

# Importation des variables de configuration
botStatus = bool(config['botStatus'])

if botStatus == False :
    quit()

def statusUpdater() :

    time.sleep(10)

    print_log("INFO", "statusUpdater processus démarré")

    while True:
        if shell.is_running():
            shell.send_command('list')
            time.sleep(0.5)
            output = shell.read_output()
            print_log('DEBUG', f"Sortie : {output}")

            pattern = r"There are (\d+) of a max of (\d+) players online"

            for line in output:
                match = re.search(pattern, line)

            if match:
                number_of_players = int(match.group(1))
                max_player = int(match.group(2))
                client.loop.create_task(client.change_presence(activity=discord.Game(name="Serveur actif, " + str(number_of_players) + '/' + str(max_player))))
                print_log('DEBUG', 'Nombre de joueurs en ligne : ' + str(number_of_players) + ' / ' + str(max_player))

            if not match :
                print_log('ERROR', 'Aucune donnée quant au nombre de joueurs')
                client.loop.create_task(client.change_presence(activity=discord.Game(name="Serveur actif")))
            
            print_log('INFO', "Statut du bot changé pour 'Serveur actif'")


        if not shell.is_running():
            client.loop.create_task(client.change_presence(activity=discord.Game(name="Serveur inactif")))
            print_log("INFO", "Statut du bot changé pour 'Serveur inactif'")

        time.sleep(120)