import os

def main(directory,prefex,file_extention=".txt"):
    # get all files in the directory
    files = os.listdir(directory)
    # filter files by extension
    # files = [f for f in files if f.endswith(file_extention)]
    # filter files by prefix
    for file in files:
            if file.endswith(file_extention):
                old_file_path=os.path.join(directory,file)
                new_file_name=prefex+file
                new_file_path=os.path.join(directory,new_file_name)
                os.rename(old_file_path,new_file_path)
                print(f"Renamed: '{file}' -> '{new_file_name}'")


if __name__ == "__main__":
    derectory="D:\cal-3d-sem\python-assignment\Renaming_Files_Directory"
    main(derectory,"old_")