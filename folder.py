import pathlib
import glob
from os.path import isdir
from file import File

class Folder:
    
    def __init__(self, path):
        self.path = path
    
    def __repr__(self):
        return f"{self.name} {self.path}"

    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, value):
        self.__path = pathlib.Path(value)
        if self.__path.absolute() and isdir(self.__path):
            self.__name = self.__path.stem
        else:
            raise "The path not is valid"
    
    def GetFiles(self):
        path_files = glob.glob(str(self.path.joinpath("**", "*.*")), recursive=True)
        return list(map(lambda x: File(x), path_files))