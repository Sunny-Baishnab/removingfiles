import time
import os 
import shutil

def main():
    path = input('enter the path')
    days = 1
    seconds = time.time()-(days*24*60*60)
    deleteFileCount = 0
    deletedFolderCount = 0

    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFolderCount = deletedFolderCount+1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)
                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolderCount = deletedFolderCount+1

                for file in files:
                    file_path = os.path.join(root_folder,file)
                    if seconds>=get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleteFileCount = deleteFileCount+1
    
            else:
                if seconds>=get_file_or_folder_age(path):
                    remove_file(path)
                    deleteFileCount= deleteFileCount+1
    else:
        print(f'"{path}"is not found')
        print('deletedFiles',deleteFileCount)
        print('deletedFolder',deletedFolderCount)

def remove_folder(path):
    if not shutil.rmtree(path):
        print('successfully removed')
    else:
        print('unable to print')    
                
def remove_file(path):
    if not os.remove(path):
        print('successfully removed')
    else:
        print('unable to print')

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__=='__main__':
    main()