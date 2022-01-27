import os

def get_file_size(folder_path):
    files_size = []


    for (path, dirs, files) in os.walk(folder_path):
        for file in files:
            filename = os.path.join(path, file)
            if os.path.isdir(folder_path):
                files_size.append(os.path.getsize(filename))
    return files_size



print(get_file_size("G:\\test"))