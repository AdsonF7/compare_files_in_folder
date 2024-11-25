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
        self.hashlist_1 = []
        self.hashlist_2 = []
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
        if self.folder_1 and self.folder_2:
            self.all_files1 = self.all_files(self.folder_1)
            self.all_files2 = self.all_files(self.folder_2)
            hashlist = list(map(lambda x: x.hash, self.all_files1))
            files = []
            for i, file in enumerate(self.all_files2):
                count = hashlist.count(file.hash)
                if count != 0: files.append(file)
            self.remove_files(files)
        elif self.folder_1:
            files = self.find_duplicates_files(self.folder_1)
            self.remove_files(files)

    def find_duplicates_files(self, folder):
        folder = Folder(folder, "**", "*.*")
        hashlist = []
        duplicates = []
        for path_file in folder.GetFiles():
            file = File(path_file)
            count = hashlist.count(file.hash)
            if count == 0: hashlist.append(file.hash)
            else: duplicates.append(file)
        return duplicates
    
    def remove_files(self, files):
        for file in files:
            os.remove(file.path)

    def all_files(self, folder):
        path_folder = pathlib.Path(folder, "**", "*.*")
        path_files = glob.glob(str(path_folder), recursive=True)
        files = []
        for path_file in path_files:
            file = File(path_file)
            files.append(file)
        return files


    
    
app = App()          
#app.folder_1 = "E:\\Nova pasta\\musicas"              
#app.folder_2 = "E:\\Nova pasta\\jpg\\jpg - Copia"
#app.folder_1 = "C:\\Users\\sonia\\Desktop\\Nova pasta - Copia"             
#app.folder_2 = "C:\\Users\\sonia\\Desktop\\Nova pasta" 
#app.find()
#input
