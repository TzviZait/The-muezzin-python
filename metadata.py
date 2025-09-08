

from pathlib import Path

from datetime import datetime


class Metadata:

    def __init__(self):
        pass

    def file_path(self,file_path):
        return file_path

    def file_name(self,file):
        file_path = Path(file)
        file_name = file_path.name
        return file_name

    def file_size(self,file):
        file_path = Path(file)
        file_size = file_path.stat().st_size
        return file_size

    def creation_file(self,file):
        file_path = Path(file)
        creation_file = file_path.stat().st_ctime
        file_timestamp = datetime.fromtimestamp(creation_file).isoformat()
        return file_timestamp


