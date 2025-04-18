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

    print_log("INFO", "statusUpdater process started")

    while True:
        if shell.is_running():
            shell.send_command('list')
            time.sleep(0.5)
            output = shell.read_output()
            print_log('DEBUG', f"Output: {output}")

            pattern = r"There are (\d+) of a max of (\d+) players online"

            for line in output:
                match = re.search(pattern, line)

            if match:
                number_of_players = int(match.group(1))
                max_player = int(match.group(2))
                client.loop.create_task(client.change_presence(activity=discord.Game(name="Server online, " + str(number_of_players) + '/' + str(max_player))))
                print_log('DEBUG', 'Number of connected players : ' + str(number_of_players) + ' / ' + str(max_player))

            if not match :
                print_log('ERROR', 'No data related to the number of connected players')
                client.loop.create_task(client.change_presence(activity=discord.Game(name="Server online")))
            
            print_log('INFO', "Bot status changed to 'Server online'")


        if not shell.is_running():
            client.loop.create_task(client.change_presence(activity=discord.Game(name="Server offline")))
            print_log("INFO", "Bot status changed to 'Server offline'")

        time.sleep(120)