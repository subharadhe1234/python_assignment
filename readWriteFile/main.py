with open("input.txt","r") as r:
    with open("output.txt","w") as w:
        w.write(r.read())
        w.close()

    r.close()