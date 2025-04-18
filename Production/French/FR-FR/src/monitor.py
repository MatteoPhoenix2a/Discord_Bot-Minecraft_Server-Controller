# Importation des librairies
import time
from src.shellController import shell
from src.config import config
from src.logger import print_log


# Importation des variables de configuration
timeOut = int(config['timeOut'])

if timeOut == 0 :
    print_log('INFO', 'Monitoring désactivé')
    quit()


#
# Définition de la fonction monitoring
#
def noPlayerMonitoring():
   
    time.sleep(10)

    print_log("INFO", "noPlayerMonitoring processus démarré")

    start_time = time.time()

    while True:
        if shell.is_running():
            shell.send_command('list')
            time.sleep(0.5)
            output = shell.read_output()
            print_log('DEBUG', f"Output: {output}")
            players = [line for line in output if 'There are' in line]

            if any('There are 0 of a max' in p for p in players):
                
                
                if time.time() - start_time >= timeOut * 60:
                    print_log('INFO', 'Aucun joueur détecté depuis 20 minutes, arrêt du serveur')
                    time.sleep(60)
                    
                    if any('There are 0 of a max' in p for p in players):
                        shell.stop_gracefully()
                    
                    if not any('There are 0 of a max' in p for p in players):
                        print_log('INFO', "Un joueur s'est reconnecté pendant la procédure, arrêt de la procédure")

                else :
                    print_log('INFO', 'Aucun joueur détecté, encore ' + str(int(timeOut - (time.time() - start_time) / 60)) + " minutes avant l'arrêt")
                    time.sleep(60)
            
            if not any('There are 0 of a max' in p for p in players):
                start_time = time.time()
                print_log('DEBUG', 'Joueur détecté, timer réinitialisé')
                time.sleep(60)

        if not shell.is_running():
            print_log('DEBUG', 'Le serveur est éteint, monitoring mis en pause pendant 2 minutes')
            time.sleep(120)