import random

def generate_large_data(file_path, num_integers):
    try:
        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write 10 million random integers to the file
            for _ in range(num_integers):
                file.write(f"{random.randint(1, 1000000)}\n")
        
        print(f"File '{file_path}' with {num_integers} random integers generated successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    # Example usage
    file_path = 'random_numbers.txt'  # Replace with your file path
    num_integers = 10000000  # 10 million integers

    generate_large_data(file_path, num_integers)
