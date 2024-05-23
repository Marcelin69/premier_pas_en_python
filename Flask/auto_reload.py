from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class RestartOnChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command)
    
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            self.restart_process()
    
    def restart_process(self):
        self.process.terminate()
        self.process.wait()
        self.process = subprocess.Popen(self.command)

if __name__ == "__main__":
    path = "."
    command = ["python", "app.py"]
    event_handler = RestartOnChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
