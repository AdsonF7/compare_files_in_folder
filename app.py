import glob
import pathlib
import os
from file import File
from folder import Folder
from gui import GUI

class App():

    def __init__(self):
        self.__gui = GUI(self)
        self.__gui.mainloop()

    def find(self, folder_1, folder_2=None, erase=False):
        if folder_1 and folder_2:
            try:
                folder1_files = Folder(folder_1).GetFiles()
                folder2_files = Folder(folder_2).GetFiles()
            except Exception: return None
            set1 = set(map(lambda x: x.hash, folder1_files))
            set2 = set(map(lambda x: x.hash, folder2_files))
            copies = set1.intersection(set2)
            if len(copies) > 0:
                files = list(filter(lambda x: x.hash in copies, folder2_files))
        elif folder_1:
            files = self.find_duplicates_files(folder_1)
        if len(files) > 0:
            if erase: self.remove_files(files)
            return True
        return False
    
    def find_duplicates_files(self, folder_path):
        folder = Folder(folder_path)
        hashlist = []
        duplicates = []
        for file in folder.GetFiles():
            count = hashlist.count(file.hash)
            if count == 0: hashlist.append(file.hash)
            else: duplicates.append(file)
        return duplicates
    
    def remove_files(self, files):
        map(lambda x: os.remove(x.path), files)

    def valid_paths(self, path_list):
        if len(path_list) > 1: return True
        return False
    
App()
#app.folder_1 = "E:\\Nova pasta\\musicas"              
#app.folder_2 = "E:\\Nova pasta\\jpg\\jpg - Copia"
#app.folder_1 = "C:\\Users\\sonia\\Desktop\\Nova pasta - Copia"             
#app.folder_2 = "C:\\Users\\sonia\\Desktop\\Nova pasta" 
#app.find()
#input
