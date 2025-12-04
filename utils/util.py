
def open_file(file_name, mode='r'):
    with open(file_name, mode) as file:
        lines = file.readlines()
        contents = [line.rstrip('\n') for line in lines]
        return contents
