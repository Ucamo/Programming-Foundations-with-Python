import os
import string
def rename_files():
    #(1) get file names from a folder
    file_list= os.listdir(r"F:\Phyton_Projects\prank")
    print(file_list)
    saved_path= os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"F:\Phyton_Projects\prank")
    #(2) for each file, rename filename
    translation = str.maketrans("", "", string.digits)
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(translation))
        os.rename(file_name,file_name.translate(translation))

    os.chdir(saved_path)

rename_files()
