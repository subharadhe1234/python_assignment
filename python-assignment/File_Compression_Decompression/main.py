import zipfile
# zip the file
def zip(input_file,zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zip:
        zip.write(input_file)
        print(f"File {input_file} has been zipped to {zip_file}")
        return zip_file
        

# unzip file
def unzip(zip_file,unzip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(unzip_file)
        print(f"File {zip_file} has been unzipped to {unzip_file}")


def main():
    input_file = "input.txt"
    zip_file = "zipped.zip"
    unzip_file = "unzipped"
    zip(input_file,zip_file)
    unzip(zip_file,unzip_file)

if __name__ == "__main__":
    main()