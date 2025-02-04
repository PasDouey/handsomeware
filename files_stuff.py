import os

# Get files in the current directory
def check_files_existence_in_direc():
    current_direct = os.getcwd()
    files = []
    for file in os.listdir(current_direct):
        files.append(file)
    return files

# Filter files by extension
def files_extension(files_direc, extension = ".txt"):
    filtred_list = []
    for fi in files_direc:
        _, file_extension = os.path.splitext(fi)
        if file_extension == extension:
            filtred_list.append(fi)
    return filtred_list
