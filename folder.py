import pathlib
import glob
from os.path import isfolder
class Folder:
    
    def __init__(self, path):
        self.path = path
        
    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, value):
        self.__path = pathlib.Path(value)
        if self.__path.absolute() and isfolder(self._path):
            self.__name = self.__path.stem
        else:
            raise "The path not is valid"
    
    def GetFiles(self):
        return glob.glob(str(self.path), recursive=True)