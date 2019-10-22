from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from fileType import filedict

import os


class Handler(FileSystemEventHandler):
    def __init__(self, tracked_folder, dest_folder):
        self.tFolder = tracked_folder
        self.dFolder = dest_folder

    def on_modified(self, event):
        for filename in os.listdir(self.tFolder):

            is_File = os.path.isfile(self.tFolder + '\\' + filename)
            if is_File:

                try:
                    ext = str(os.path.splitext(
                        self.tFolder + '\\' + filename)[1])

                    if ext not in filedict:
                        ext = 'noname'

                except Exception:
                    ext = 'noname'

                self.dFolder = filedict[ext]
                src = self.tFolder + "\\" + filename
                new_dest = self.dFolder + "\\" + filename
                os.rename(src, new_dest)
