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
        return self._path
    
    @path.setter
    def path(self, value):
        self._path = pathlib.Path(value)
        if self._path.absolute() and isdir(self._path):
            self._name = self._path.stem
        else:
            raise "The path not is valid"
    
    @property
    def files(self):
        path_files = [file for file in self.path.rglob("*.*") if file.is_file()]
        return list(map(lambda x: File(x), path_files))