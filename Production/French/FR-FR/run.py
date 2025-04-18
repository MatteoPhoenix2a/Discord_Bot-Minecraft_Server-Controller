 # Importation des librairies
from src.config import config
from src.logger import print_log
from src.shellController import shell
from src.monitor import noPlayerMonitoring
from src.status import statusUpdater
from src.bot import client
import threading

#
# Lancement du programme
#

# On lance le monitoring dans un thread dédié
monitoring_thread = threading.Thread(target=noPlayerMonitoring, daemon=True)
monitoring_thread.start()

# On lance le status dans un thread dédié
statut_thread = threading.Thread(target=statusUpdater, daemon=True)
statut_thread.start()


# On lance le Bot
client.run(config['token'])