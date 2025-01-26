
def char_word_in_file(input_file,output_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
        no_line=len(data)
        char_count=0
        word_count=0
        for line in data:
            words = line.split()
            char_count+=len(line)
            word_count+=len(words)
            with open(output_file, 'w') as f:
                f.write(f"no of lines: {str(no_line)}\n")
                f.write(f"no of words: {str(word_count)}\n")
                f.write(f"no of characters: {str(char_count)}\n")



def main():
    input_file="input1.txt"
    output_file="output.txt"
    char_word_in_file(input_file,output_file)
    

                
if __name__=="__main__":
    main()