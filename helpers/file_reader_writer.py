class readerWriter:
    def __init__(self, location):
        self.location = location

    def open_file(self):
        with open(self.location) as file:
            pass
            #print(file.read())
        return file
    
    def dictionary_reader(self):
        dict = {}
        with open(self.location) as file:
            for line in file:
                keyvalue1, var = line.partition("=")[::2]
                dict[keyvalue1.strip()] = str(var)

        return dict

    def close_file(self, file):
        file.close()

    def get_connection_string(self):
        myfile = readerWriter(self.location)
        myfile.open_file()
        results = myfile.dictionary_reader()
        return results.get('connection_string')