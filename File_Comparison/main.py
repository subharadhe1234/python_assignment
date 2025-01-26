
def main():
    try:
        with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
            for line_num, (line1, line2) in enumerate(zip(f1, f2), start=1):
                if line1 != line2:
                    print(f"Difference found at line {line_num}:")
                    print(f"File1: {line1.strip()}")
                    print(f"File2: {line2.strip()}")
    except Exception as e:
        print("An error occurred: ", str(e))



if __name__ == "__main__":
    main()