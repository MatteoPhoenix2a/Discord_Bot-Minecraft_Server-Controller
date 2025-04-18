# Importation des librairies
from datetime import date, datetime
from zoneinfo import ZoneInfo
import os
import tarfile
import shutil
from src.config import config


# Importation des varibles de configurations
log_level = config['log_level']
timezone = ZoneInfo(config['timezoneName'])
logCompression = bool(config['logCompression'])


#
# Définition du système de LOGS
#

# Vérification de la présence du dossier de log
if os.path.isdir('logs') :
    print('Dossier de logs détecté')
if not os.path.isdir('logs') :
    print('Dossier de logs non détecté, création en cours')
    os.mkdir('logs')
    print('Dossier de logs créé')

# On crée le sous-dossier puis le fichier de log avec la date du jour
if os.path.isdir('logs/' + str(date.today())) :
    print('Le dossier de logs du jour existe déjà')
if not os.path.isdir('logs/' + str(date.today())) :
    print("Le dossier du log du jour n'existe pas, création en cours")
    os.mkdir('logs/' + str(date.today()))
    print("Le dossier de log du jour a été créé")

file = open('logs/' + str(date.today()) + '/' + str(datetime.now(timezone).strftime('%Y-%m-%dT%H-%M-%S%z')) + '.txt', 'w')

# Compression des dossiers de logs périmés
if logCompression == True :
    for folder in os.listdir('logs'):
        if folder != str(date.today()) and not '.gz' in folder :
            with tarfile.open('logs/' + folder + '.tar.gz', 'w:gz') as tar:
                tar.add('logs/' + folder, arcname=os.path.basename('logs/' + folder))
                print('Archivage du dossier ' + folder)
                shutil.rmtree('logs/' + folder)
                print('Supression du dossier ' + folder)

# On regarde si le niveau de log est réglé sur 'PRODUCTION' 
if 'PRODUCTION' in log_level:
    log_level.append('INFO' and 'ERROR' and 'WARNING')
    print('Mode production')
    file.write('Mode production\n')

# On crée la fonction appelée pour les logs
def print_log(level, content):
    print('[' + str(datetime.now(timezone).strftime('%H:%M:%S%z')) + '] ' + level + ': ' + content)
    
    if 'NONE' in log_level:
        print('Logs désactivés')

    elif 'ALL' in log_level:
        file.write('[' + str(datetime.now(timezone).strftime('%H:%M:%S%z')) + '] ' + level + ': ' + content + '\n')
    
    elif 'INFO' in log_level and level == 'INFO':
        file.write('[' + str(datetime.now(timezone).strftime('%H:%M:%S%z')) + '] ' + level + ': ' + content + '\n')
    
    elif 'ERROR' in log_level and level == 'ERROR':
        file.write('[' + str(datetime.now(timezone).strftime('%H:%M:%S%z')) + '] ' + level + ': ' + content + '\n')
    
    elif 'WARNING' in log_level and level == 'WARNING':
        file.write('[' + str(datetime.now(timezone).strftime('%H:%M:%S%z')) + '] ' + level + ': ' + content + '\n')
    
    elif 'DEBUG' in log_level and level == 'DEBUG':
        file.write('[' + str(datetime.now(timezone).strftime('%H:%M:%S%z')) + '] ' + level + ': ' + content + '\n')
    
    if level not in ['ALL', 'INFO', 'ERROR', 'WARNING', 'DEBUG']:
        print('Log level invalide')
        file.write('[' + str(datetime.now(timezone).strftime('%H:%M:%S%z')) + '] ' + 'Log level invalide\n')

