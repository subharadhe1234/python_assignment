import json
import pandas as pd 

def main():
    input_file="input.json"
    with open(input_file,"r") as file:
        data = json.load(file)
        for i in data:
            print(f"ID:  {i['ID']}")
            print(f"Name:  {i['Name']}")
            print(f"Email:  {i['Email']}")
            print("-"*20)
            

if __name__ == "__main__":
    main()