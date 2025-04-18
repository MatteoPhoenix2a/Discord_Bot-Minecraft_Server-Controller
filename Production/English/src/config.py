# Libraries importations
import json
import os
from zoneinfo import ZoneInfo

#
# We are importing variables from the JSON file
#

# We are checking the JSON configuration file presence
if os.path.isfile('config.json') :
    print('Configuration file detected')

if not os.path.isfile('config.json') :
    print('Configuration file not detected, creation in progress')
    base_config = {
        'token': 'INSERT_TOKEN',
        'log_level': ['PRODUCTION'],
        'javaFileName': 'INSERT_.jar_File',
        'pathToFile': 'INSERT_PATH_HERE',
        'serverIp': 'INSERT_IP_HERE',
        'timezoneName': 'INSERT_TIMEZONE_HERE',
        'timeOut': 30,
        'logCompression': 'True',
        'botStatus': 'True',
        'baseUserRole': 'Minecraft',
        'adminRole': 'Admin',
        'pingCommand': 'ping',
        'helpCommand': 'help',
        'ipServerCommand': 'ip',
        'startServerCommand': 'start server',
        'stopServerCommand': 'stop server',
        'restartServerCommand': 'restart server',
        'whitelistCommand': 'add me'
        }
    with open('config.json', 'w') as file:
        json.dump(base_config, file, indent=4)
        print('Configuration file created')
        print('Please fill the configuration file before starting the bot')
        quit()


# We are importing JSON file's parameters
with open('config.json', 'r') as file:
    config = json.load(file)

try :
    token = config['token']
    log_level = config['log_level']
    javaFileName = config['javaFileName']
    pathToFile = config['pathToFile']
    serverIp = config['serverIp']
    timezone = ZoneInfo(config['timezoneName'])
    timeOut = int(config['timeOut'])
    logCompression = bool(config['logCompression'])
    botStatus = bool(config['botStatus'])
    baseUserRole = config['baseUserRole']
    adminRole = config['adminRole']
    pingCommand = config['pingCommand']
    helpCommand = config['helpCommand']
    ipServerCommand = config['ipServerCommand']
    startServerCommand = config['startServerCommand']
    restartServerCommand = config['restartServerCommand']
    stopServerCommand = config['stopServerCommand']
    whitelistCommand = config['whitelistCommand']

except :
    print('Error while loading the configuration file')
    quit()