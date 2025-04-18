 # Importation des librairies
from src.config import config
from src.logger import print_log
from src.shellController import shell
from src.monitor import noPlayerMonitoring
from src.status import statusUpdater
from src.bot import client
import threading

#
# Programm Launch
#

# We start monitoring in a dedicated thread
monitoring_thread = threading.Thread(target=noPlayerMonitoring, daemon=True)
monitoring_thread.start()

# We start bot status in a dedicated thread
statut_thread = threading.Thread(target=statusUpdater, daemon=True)
statut_thread.start()


# We start the bot
client.run(config['token'])