import json

dict={}
with open("wordlist.txt","r") as infile:
    word=infile.readline();
    while(word):
        lList=[letter for letter in word]
        lList.sort()
        lList=lList[1:]
        key=""
        for letter in lList:
            key=key+letter
        print (key)
        dict.update({key:word[:-1]})
        word=infile.readline();
    print (dict)
    infile.close()
with open("data.clx","w") as outfile:
    json.dump(dict,outfile)
