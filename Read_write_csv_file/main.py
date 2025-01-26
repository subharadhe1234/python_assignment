import pandas as pd

def main():
    input_file="input.csv"
    output_file="output.csv"
    try:
        df=pd.read_csv(input_file)
        df["Email"]=df["Email"].str.replace("@example.com", "@newdomain.com", regex=False)
        df.to_csv(output_file, index=False)
        print(f"File '{input_file}' has been modified and saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()