# Libraries importations
import subprocess
import threading
import queue
import time
from typing import List, Optional
from src.config import config
from src.logger import print_log


# Importation of the configurations variables
javaFileName = config['javaFileName']
pathToFile = config['pathToFile']


#
# Shell class definition
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
        #Read the standar output of the processus in a thread.
        for line in iter(self.process.stdout.readline, ''):
            if line:
                self.output_queue.put(line.strip())
            else:
                break

    def _send_commands_loop(self):
        # If you want to process differed commands.
        while self.running and self.process.poll() is None:
            try:
                command = self.command_queue.get(timeout=0.2)
                self.send_command(command)
            except queue.Empty:
                continue

    def start(self):
        # Starting the processus and the associated threads.
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
        # Sending immediatly a command through stdin, if the processus alive/online.
        if self.is_running() and self.process.stdin:
            try:
             self.process.stdin.write(command + '\n')
             self.process.stdin.flush()
            except BrokenPipeError:
             print_log('ERROR', "Le processus n'est plus accessible (BrokenPipeError).")

    def queue_command(self, command: str):
        # Add a command executed later.
        self.command_queue.put(command)

    def read_output(self) -> List[str]:
        # Get all the output lines possibles.
        lines = []
        while not self.output_queue.empty():
            lines.append(self.output_queue.get())
        return lines

    def is_running(self) -> bool:
        # Check if the processus still alive.
        return self.process is not None and self.process.poll() is None

    def stop_gracefully(self, wait_time: int = 10):
        # stop properly the server whith the 'stop' command.
        # Wait until wait_time seconds for the processus to stop.
        if self.is_running():
            self.send_command('stop')
            for _ in range(wait_time * 10):
                if not self.is_running():
                    break
                time.sleep(0.1)

    def stop(self):
        # Immediately stopping the processus (without the 'stop' command).
        self.running = False
        if self.process:
            self.process.terminate()
            self.process.wait()

# Definition of the Shell parameters
command = ['java', '-jar', javaFileName]
shell = InteractiveShellController(command, pathToFile) 