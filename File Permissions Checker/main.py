import os
import stat

def check_permissions(file_path):
    """Check if a file has insecure permissions."""
    try:
        # Get the file's status using os.stat()
        file_stat = os.stat(file_path)
        
        # Get the file's mode (permissions)
        file_permissions = file_stat.st_mode
        
        # Check if the file is world-writable (writeable by others)
        if file_permissions & stat.S_IWOTH:
            return "world-writable"
        
        # Check if the file is executable by others, or has any other risky permissions
        if file_permissions & stat.S_IXOTH:
            return "executable by others"
        
        return "secure"
    
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"

def scan_directory(directory_path):
    """Scan a directory and identify files with insecure permissions."""
    insecure_files = []
    
    # Iterate over files in the directory
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            permission_status = check_permissions(file_path)
            
            if permission_status != "secure":
                insecure_files.append((file_path, permission_status))
    
    return insecure_files


if __name__ == "__main__":
    # Example usage
    directory_path = r'D:\cal-3d-sem\python-assignment'  
    insecure_files = scan_directory(directory_path)

    if insecure_files:
        print("Insecure files found:")
        for file, status in insecure_files:
            print(f"File: {file} - Risk: {status}")
    else:
        print("No insecure files found.")
