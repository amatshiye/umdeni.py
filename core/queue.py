import os.path
from typing import List

from core.song import Song


class Queue:
    def __int__(self, new_songs: List[Song]):
        self.songs_folder = "songs_folder"
        self.songs: List[Song] = new_songs

        # check if downloaded songs folder exists
        self.songs_folder_exists()

        # if folder is not empty delete items inside

    def songs_folder_exists(self):
        path_to_folder = os.path.isdir(self.songs_folder)

        if not path_to_folder:
            os.makedirs(self.songs_folder)
            print(f"{self.songs_folder} has been created.")
        else:
            print(f"{self.songs_folder} folder already exists.")

    def is_songs_folder_empty(self) -> bool:
        if not any(os.scandir(self.songs_folder)):
            return True
        else:
            return False
