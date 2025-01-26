input_file=["file1.txt","file2.txt","file3.txt"]
output_file="marge.txt"

try:
    with open(output_file,"w") as w:
        for file in input_file:
            with open(file,"r") as r:
                w.write(r.read()+"\n")

except FileNotFoundError as e:
    print(f"An error occurred: {e}")

except Exception as e:
    print(f"An error occurred: {e}")


