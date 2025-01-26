
def add_inc(map,value):
    if value in map.keys():
        map[value]=map[value]+1
    else:
        map[value]=0


def sort_dec(map):
    list=dict(sorted(map.items(),key=lambda item: item[1],reverse=True))
    return list

def print_dict(map):
    for key,_ in map.items():
        print(key)

def file_write(list):
    with open("output.txt","w") as w:
        for key,_ in list.items():
            w.write(key+"\n")
        w.close()

def main():
    with open("input.txt","r") as r:
        data=r.read()
        words=[]
        word=""
        i=0
        flag=0
        map={}
        while(i<len(data)):
            c=data[i]
            if(c==" " or c=="\n"):
                words.append(word)
                add_inc(map,word)
                word=""
                # skip  space and enter exces 
                while((c==" " or c=="\n") and i<len(data)):
                    c=data[i]
                    i=i+1
                    flag=1
            word=word + c
            if flag==0:
                i=i+1
            else:
                flag=0
        print(f"length of words: {len(words)}")
        list=sort_dec(map)
        file_write(list)
        
        r.close()

if __name__=="__main__":
    main()