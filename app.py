import glob
import pathlib
import os
from file import File
from folder import Folder
from gui import GUI

class App():

    def __init__(self):
        self.__gui = GUI(self)
        self.folder_1 = None
        self.folder_2 = None
        self.__gui.mainloop()

    @property
    def folder_1(self):
        return self.__folder_1

    @property
    def folder_2(self):
        return self.__folder_2
    
    @folder_1.setter
    def folder_1(self, value):
        self.__folder_1 = value

    @folder_2.setter
    def folder_2(self, value):
        self.__folder_2 = value
    
    def find(self, folder_1, folder_2=None):
        if folder_1 and folder_2:
            folder1_files = Folder(folder_1).GetFiles()
            folder2_files = Folder(folder_2).GetFiles()
            set1 = set(map(lambda x: x.hash, folder1_files))
            set2 = set(map(lambda x: x.hash, folder2_files))
            files = []
            for i, file in enumerate(folder2_files):
                if file.hash in set1.intersection(set2): files.append(file)
            self.remove_files(files)
        elif folder_1:
            files = self.find_duplicates_files(folder_1)
            self.remove_files(files)

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


    
    
#app.folder_1 = "E:\\Nova pasta\\musicas"              
#app.folder_2 = "E:\\Nova pasta\\jpg\\jpg - Copia"
#app.folder_1 = "C:\\Users\\sonia\\Desktop\\Nova pasta - Copia"             
#app.folder_2 = "C:\\Users\\sonia\\Desktop\\Nova pasta" 
#app.find()
#input
