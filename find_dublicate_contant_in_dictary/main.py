import os
import  hashlib


# find hash value
def get_file_hash(input_file):
    hash_sha256=hashlib.sha256() # hash  object 
    with open(input_file, 'rb') as f:
        # read file in binary format
        while chuck:= f.read(4096):
            hash_sha256.update(chuck)
    return hash_sha256.hexdigest()


# find dublicate
def find_duplicate(directory):
    file_hash={}
    dublicate=[]
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path=os.path.join(root, file)
            hash=get_file_hash(file_path)
            if hash in file_hash:
                dublicate.append((file_hash[hash],file_path))
            else:
                file_hash[hash]=file_path
        # print(root,dir,files)

    return dublicate



def main():
    directory = r"D:\cal-3d-sem\python-assignment\find_dublicate_contant_in_dictary"
    dublicate=find_duplicate(directory)
    for item in dublicate:
        print(f"Orginal: {item[0]},\nDublicate: {item[1]}\n")


if __name__ == "__main__":
    main()