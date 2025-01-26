import os

def main(directory,indent=0):
    
    for filename in os.listdir(directory):

        item_path = os.path.join(directory, filename)

        print("  " * indent + "j|-- " + filename)
        if os.path.isdir(item_path):

            main(item_path,indent+1)
            
        

if __name__ == "__main__":
    directory="D:\cal-3d-sem\python-assignment"
    print("\nDirectory structure:")
    main(directory=directory)