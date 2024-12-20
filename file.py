import pathlib
import hashlib
import pathlib
from os.path import isfile

class File():

    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"{self.hash} {self.name} {self.path}"

    @property
    def name(self):
        return self.__name

    @property
    def path(self):
        return self.__path
    
    @property
    def hash(self):
        return self.__hash

    @path.setter
    def path(self, value):
        self.__path = pathlib.Path(value)
        if self.__path.is_absolute() and isfile(self.__path):
            self.__name = self.__path.name
            self.__hash = File.checksum_md5(self.__path)
        else:
            raise "The path not is valid"
    
    @staticmethod
    def checksum_md5(file):
        data = ""
        with open(file, "rb") as file_to_check:
            file_hash = hashlib.md5()
            while chunk := file_to_check.read(8192):
                file_hash.update(chunk)
                chunk = file_to_check.read(8192)
            file_to_check.close()
        return file_hash.hexdigest()
