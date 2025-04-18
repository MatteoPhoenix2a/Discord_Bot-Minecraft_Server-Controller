# Importation des librairies
import time
from src.shellController import shell
from src.config import config
from src.logger import print_log


# Importation des variables de configuration
timeOut = int(config['timeOut'])

if timeOut == 0 :
    print_log('INFO', 'Monitoring disabled')
    quit()


#
# Définition de la fonction monitoring
#
def noPlayerMonitoring():
   
    time.sleep(10)

    print_log("INFO", "noPlayerMonitoring process started")

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
                    print_log('INFO', 'No player detected for 20 minutes, shutting down the server')
                    time.sleep(60)
                    
                    if any('There are 0 of a max' in p for p in players):
                        shell.stop_gracefully()
                    
                    if not any('There are 0 of a max' in p for p in players):
                        print_log('INFO', 'A player reconnected while the stop procedure, the process aborted')

                else :
                    print_log('INFO', 'No player detected, waiting ' + str(int(timeOut - (time.time() - start_time) / 60)) + ' minutes before shutdown')
                    time.sleep(60)
            
            if not any('There are 0 of a max' in p for p in players):
                start_time = time.time()
                print_log('DEBUG', 'Player detected, resetting timer')
                time.sleep(60)

        if not shell.is_running():
            print_log('DEBUG', 'Server is not running, monitoring stopped for 2 minutes')
            time.sleep(120)