import os


class DAL:

    def __init__(self,file_path):
        self.file_path = file_path

    def dal(self):
        my_list = []
        for file in os.listdir(self.file_path):
            full_path = os.path.join(self.file_path,file)
            my_list.append(full_path)
        return my_list


