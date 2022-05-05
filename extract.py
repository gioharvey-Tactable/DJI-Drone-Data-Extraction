import os
from zipfile import ZipFile
from datetime import datetime
import shutil


# https://flaviocopes.com/python-get-file-details/
# https://www.geeksforgeeks.org/working-zip-files-python/
# https://pynative.com/python-move-files/


def createDirectory(path: str):
    if not os.path.exists(path):
        print(f"Making Folder : {path}")
        os.mkdir(path)

def deleteDirectory(dir_to_delete: str):
    shutil.rmtree(dir_to_delete) # delete the directory and recursively all the files in the directory
    print(f"Deleted Folder {dir_to_delete}")

def zipFiles(dir_to_write: str, files:list = None):
    """ Zip Folder Provided By User """
  
    shutil.make_archive(dir_to_write, 'zip', dir_to_write) # Name of zip, type to zip, folder_to_zip
    print(f'All Files were zipped for {dir_to_write}')

def unzipFiles():
    """Not yet implemented"""
    pass

def moveFiles(base_path: str, data_dict:dict = None):
    
    curr_dir = os.getcwd()
    for date_path in data_dict:
        createDirectory(f'{curr_dir}/{date_path}')
        print(f"Running process for: {date_path}")
        for file_type in data_dict[date_path]:
            createDirectory(f"{curr_dir}/{date_path}/{file_type}")
            
            # for eg: your working directory/date/MP4 
            base_destination = f"{curr_dir}/{date_path}/{file_type}" 
            
            files_path = data_dict[date_path][file_type]
            for source in files_path:
                filename = source.split("/")[-1] # Get the filename
                
                destination = f"{base_destination}/{filename}" # If I wanted to the full file to copy

                print(date_path, file_type, source, destination)

                # Copy to
                shutil.move(source, destination) # Copy files to folder 
        
        zipFiles(date_path) # zip files
        deleteDirectory(date_path) # Delete Directories

def extensionsSplit(base_path: str, date_dirs: dict):
    """Split Files Via Extensions"""
    file_ext = ['JPG', 'MP4', 'DNG']

    for date_dir in date_dirs:        
        files = date_dirs[date_dir]
        jpegs = list(filter(lambda x: x.endswith(file_ext[0]), files))
        mp4 = list(filter(lambda x: x.endswith(file_ext[1]), files))
        dng = list(filter(lambda x: x.endswith(file_ext[2]), files))
        
        date_dirs[date_dir] = {
            "jpegs".upper(): jpegs,
            "mp4".upper(): mp4,
            "dng".upper(): dng
        }
    moveFiles(base_path,date_dirs)
    
def splitFilesToTimeDirectories(base_paths:str, files):
    """ Make the Files into Directories based on time"""
    # time_scale: list of files
    time_directory = {}
    
    for file in files:
        file_p = f"{base_paths}/{file}"
        last_mod = os.path.getmtime(file_p)
        created = os.path.getctime(file_p)
        
        # %H:%M:%S' to add the hours  
        date_string = datetime.fromtimestamp(last_mod).strftime('%Y-%m-%d') # Convert to More readable datetime
        
        if date_string in time_directory:
            time_directory[date_string].append(file_p) # Not the First Addition
        else:
            time_directory[date_string] = [file_p] # The First Addition 
    
    extensionsSplit(base_paths, time_directory)

def retrieveFiles(media_directory: str = ""):
    
    if media_directory:
        _paths = ['100MEDIA', 'PANORAMA']

        paranorma_paths = f"{media_directory}/{_paths[1]}" # Paranorma Folder
        media_paths = f"{media_directory}/{_paths[0]}" # Media Folder

        curr_dir = os.getcwd()
        print(curr_dir)

        media_files = list(os.listdir(media_paths))
        paranorma_files = list(os.listdir(paranorma_paths)) # NOTE: SOON TO COME

        splitFilesToTimeDirectories(media_paths, media_files)

