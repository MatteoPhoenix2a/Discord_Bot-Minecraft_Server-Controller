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
        'version' : '1.1.0',
        'token': 'INSERT_TOKEN',
        'log_level': ['PRODUCTION'],
        'javaFileName': 'INSERT_.jar_FILE',
        'pathToFile': 'INSERT_PATH_HERE',
        'serverIp': 'INSERT_IP_HERE',
        'timezoneName': 'INSERT_TIMEZONE_HERE',
        'language' : 'EN',
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
    language = config['language']
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

# We are importing language parameters
with open('languages/' + language + '.json', 'r') as language_file:
    language_config = json.load(language_file)

try :
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

except :
    print("Error while loading the language file. Please check your 'language' is correct in your config.json file")
    quit()