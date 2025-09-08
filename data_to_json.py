from metadata import Metadata




class DataToJson:

    def __init__(self):
        self.data = Metadata()


    def data_to_dict(self,dict_file):
        my_list = []
        my_dict = {}
        for file in dict_file:

            my_dict[self.data.file_name(file) +" "+ str(self.data.file_size(file))] = \
                {
                  "file_path":file,
                  "file_name":self.data.file_name(file),
                  "file_size":self.data.file_size(file),
                  "creation_file":self.data.creation_file(file)
                 }
            my_list.append(my_dict)
            my_dict = {}
        return my_list


