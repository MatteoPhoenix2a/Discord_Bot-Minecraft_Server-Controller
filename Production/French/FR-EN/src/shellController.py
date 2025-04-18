# Importation des librairies
import subprocess
import threading
import queue
import time
from typing import List, Optional
from src.config import config
from src.logger import print_log


# Importation des variables de configuration
javaFileName = config['javaFileName']
pathToFile = config['pathToFile']


#
# Définition de la classe Shell
#
class InteractiveShellController:
   
    def __init__(self, command: List[str], cwd: Optional[str] = None):
        self.command = command
        self.cwd = cwd
        self.process: Optional[subprocess.Popen] = None
        self.output_queue = queue.Queue()
        self.reader_thread = None
        self.command_queue = queue.Queue()
        self.command_thread = None
        self.running = False

    def _read_stdout(self):
        # Lit la sortie standard du processus dans un thread.
        for line in iter(self.process.stdout.readline, ''):
            if line:
                self.output_queue.put(line.strip())
            else:
                break

    def _send_commands_loop(self):
        # Si l'on veut envoyer des commandes en diférées.
        while self.running and self.process.poll() is None:
            try:
                command = self.command_queue.get(timeout=0.2)
                self.send_command(command)
            except queue.Empty:
                continue

    def start(self):
        # Démarre le processus et les threads associés.
        self.process = subprocess.Popen(
            self.command,
            cwd=self.cwd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        self.running = True
        self.reader_thread = threading.Thread(target=self._read_stdout, daemon=True)
        self.reader_thread.start()
        self.command_thread = threading.Thread(target=self._send_commands_loop, daemon=True)
        self.command_thread.start()

    def send_command(self, command: str):
        # Envoie immédiatement la commande via stdin, si le processus est actif.
        if self.is_running() and self.process.stdin:
            try:
             self.process.stdin.write(command + '\n')
             self.process.stdin.flush()
            except BrokenPipeError:
             print_log('ERROR', "Processus no more accessible (BrokenPipeError).")

    def queue_command(self, command: str):
        # Ajoute une commande à éxécuter plus tard.
        self.command_queue.put(command)

    def read_output(self) -> List[str]:
        # Lit toute la sortie disponible.
        lines = []
        while not self.output_queue.empty():
            lines.append(self.output_queue.get())
        return lines

    def is_running(self) -> bool:
        # Vérifie si le processus est actif.
        return self.process is not None and self.process.poll() is None

    def stop_gracefully(self, wait_time: int = 10):
        # Arrête proprement le processus avec la commande 'stop'.
        # attend pendant wait_time seconds pour que le processus s'arrête.
        if self.is_running():
            self.send_command('stop')
            for _ in range(wait_time * 10):
                if not self.is_running():
                    break
                time.sleep(0.1)

    def stop(self):
        # Arrête immédiatement le processus (sans la commande 'stop').
        self.running = False
        if self.process:
            self.process.terminate()
            self.process.wait()

# Définition des paramètres de Shell
command = ['java', '-jar', javaFileName]
shell = InteractiveShellController(command, pathToFile) 