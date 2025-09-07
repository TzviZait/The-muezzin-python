from metadata import Metadata

import os

class DataToJson:

    def __init__(self,file_path):
        self.data = Metadata(file_path)

    def data_to_dict(self):
        my_dict = {}
        for entry_name in os.listdir(self.data.file_path()):
            full_path = os.path.join(self.data.file_path(), entry_name)
            my_dict[full_path] = {"file name":self.data.file_name(full_path),
                                  "file_size":self.data.file_size(full_path),
                                  "creation_file":self.data.creation_file(full_path)}
        return my_dict


