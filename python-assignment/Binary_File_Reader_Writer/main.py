def main():
    input_file="image.jpg"
    output_file="image_mod.jpg"
    with open(input_file,"rb") as r:
        binary_data=r.read()
        modified_binary_data=binary_data.replace(b'\x00',b'\xff')
        with open(output_file,"wb") as w:
            w.write(modified_binary_data)
        


if __name__ == "__main__":
    main()