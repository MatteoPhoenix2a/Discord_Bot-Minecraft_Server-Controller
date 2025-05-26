# Libraries importations
from datetime import date, datetime
from zoneinfo import ZoneInfo
import os
import tarfile
import shutil
from src.config import config


# Configuration of the imported vaariables
log_level = config['log_level']
timezone = ZoneInfo(config['timezoneName'])
logCompression = bool(config['logCompression'])


#
# Definition of the LOG system
#

# Checking the log folder presence
if os.path.isdir('logs') :
    print('Logs directory detected')
if not os.path.isdir('logs') :
    print('Logs directory not detected, creation in progress')
    os.mkdir('logs')
    print('Logs directory created')

# We are creating the folder, and then the file with the today's date
if os.path.isdir('logs/' + str(date.today())) :
    print('Directory exists')
if not os.path.isdir('logs/' + str(date.today())) :
    print("Today's Logs directory not detected, creation in progress")
    os.mkdir('logs/' + str(date.today()))
    print("Today's Logs directory created")

file = open('logs/' + str(date.today()) + '/' + str(datetime.now(timezone).strftime('%Y-%m-%d_%H-%M-%S')) + '.txt', 'w')

# Compression of the old log folders
if logCompression == True :
    for folder in os.listdir('logs'):
        if folder != str(date.today()) and not '.gz' in folder :
            with tarfile.open('logs/' + folder + '.tar.gz', 'w:gz') as tar:
                tar.add('logs/' + folder, arcname=os.path.basename('logs/' + folder))
                print('Archiving ' + folder + ' folder')
                shutil.rmtree('logs/' + folder)
                print('Removing ' + folder + ' folder')

# We are checking if the log level set to production 
if 'PRODUCTION' in log_level:
    log_level.append('INFO' and 'ERROR' and 'WARNING')
    print('Production mode')
    file.write('Production mode\n')

# We are creating the fonction called for the logs
def print_log(level, content):
    print('[' + str(datetime.now(timezone).strftime('%m-%d-%y_%H-%M-%S_%z')) + '] ' + level + ': ' + content)
    
    if 'NONE' in log_level:
        print('Log disabled')

    elif 'ALL' in log_level:
        file.write('[' + str(datetime.now(timezone).strftime('%m-%d-%y_%H-%M-%S_%z')) + '] ' + level + ': ' + content + '\n')
    
    elif 'INFO' in log_level and level == 'INFO':
        file.write('[' + str(datetime.now(timezone).strftime('%m-%d-%y_%H-%M-%S_%z')) + '] ' + level + ': ' + content + '\n')
    
    elif 'ERROR' in log_level and level == 'ERROR':
        file.write('[' + str(datetime.now(timezone).strftime('%m-%d-%y_%H-%M-%S_%z')) + '] ' + level + ': ' + content + '\n')
    
    elif 'WARNING' in log_level and level == 'WARNING':
        file.write('[' + str(datetime.now(timezone).strftime('%m-%d-%y_%H-%M-%S_%z')) + '] ' + level + ': ' + content + '\n')
    
    elif 'DEBUG' in log_level and level == 'DEBUG':
        file.write('[' + str(datetime.now(timezone).strftime('%m-%d-%y_%H-%M-%S_%z')) + '] ' + level + ': ' + content + '\n')
    
    if level not in ['ALL', 'INFO', 'ERROR', 'WARNING', 'DEBUG']:
        print('Invalid log level')
        file.write('[' + str(datetime.now(timezone).strftime('%m-%d-%y_%H-%M-%S_%z')) + '] ' + 'Invalid log level\n')

