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
        return self._name

    @property
    def path(self):
        return self._path
    
    @property
    def hash(self):
        return self._hash

    @path.setter
    def path(self, value):
        self._path = pathlib.Path(value)
        print(self._path)
        if self._path.is_absolute() and isfile(self._path):
            self._name = self._path.name
            self._hash = File.checksum_md5(self._path)
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

