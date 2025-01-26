import hashlib

def calculate_md5(file_path):
    """Calculate the MD5 checksum of a file."""
    try:
        # Initialize the MD5 hash object
        md5_hash = hashlib.md5()

        # Open the file in binary mode and read it in chunks
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                md5_hash.update(chunk)
        
        # Return the hexadecimal MD5 checksum
        return md5_hash.hexdigest()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def verify_integrity(file_path, known_hash):
    """Verify the integrity of the file by comparing its MD5 checksum with a known hash."""
    file_hash = calculate_md5(file_path)
    
    if file_hash is None:
        return False
    
    if file_hash == known_hash:
        print("File integrity is verified: The checksum matches.")
        return True
    else:
        print("File integrity check failed: The checksum does not match.")
        return False

if __name__ == "__main__":
    # Example usage
    file_path = 'sample_file.txt'  # Replace with your file path
    known_hash = 'd41d8cd98f00b204e9800998ecf8427e'  # Example known hash (MD5)

    verify_integrity(file_path, known_hash)
