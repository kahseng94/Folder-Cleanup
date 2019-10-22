from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from fileHandler import Handler
import os
import time


folder_to_track = r"C:\Users\kahse\downloadtest"
folder_dest = r"C:\Users\kahse\downloadtest\PDF"
event_handler = Handler(folder_to_track, folder_dest)
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
