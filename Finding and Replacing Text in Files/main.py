def search_and_replace(file_path, search_text, replace_text):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Replace the search_text with replace_text
        content = content.replace(search_text, replace_text)
        
        # Open the file in write mode to save the updated content
        with open(file_path, 'w') as file:
            file.write(content)
        
        print("Text replacement completed successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    file_path = 'server.log'  # Replace with your file path
    search_text = 'ERROR'
    replace_text = 'warning'
    search_and_replace(file_path, search_text, replace_text)
