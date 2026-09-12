import os
import shutil

def set_path():
    global folder_path, file_list, png, zip, pdf, txt, mp4, pptx
    folder_path = input("Set folder path: ")
    if os.path.exists(folder_path) == True:
        print(f"Sucessfully set {folder_path}")
        file_list = os.listdir(folder_path)
        for file in os.listdir(folder_path):
            if(file.endswith('jpg')):
                print(file)
                count += 1
        return   
    else:
        print("Please set a valid path!")
    

def file_lister():
    print(file_list)
    return

folder_path = ""
file_list = []
png = 0
zip = 0
pdf = 0
txt = 0
mp4 = 0
pptx = 0

set_path()
file_lister()



