import os
import time

def display_file_metadata(directory):
    """
    Extract and display metadata (size, creation date, and modification date) for files in a directory.

    :param directory: Path to the directory containing files
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    print(f"Metadata for files in directory: {directory}\n")
    print(f"{'File Name':<30} {'Size (Bytes)':<15} {'Creation Date':<25} {'Last Modified Date':<25}")
    print("-" * 95)

    # Loop through each file in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Ensure it is a file (not a directory)
        if os.path.isfile(file_path):
            # Get file metadata using os.stat()
            file_stats = os.stat(file_path)

            # File size in bytes
            file_size = file_stats.st_size

            # Creation date and modification date (formatted)
            creation_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stats.st_ctime))
            modification_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stats.st_mtime))

            # Print metadata
            print(f"{file_name:<30} {file_size:<15} {creation_date:<25} {modification_date:<25}")

# Example usage
if __name__ == "__main__":
    # Provide the directory path
    directory_path = r"D:\cal-3d-sem\python-assignment\readWriteFile"
    display_file_metadata(directory_path)
