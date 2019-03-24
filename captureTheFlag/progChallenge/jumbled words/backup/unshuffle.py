import json
import os


def process(jumbled):
    jumbled=[letter for letter in jumbled]
    jumbled.sort()
    str=""
    for letter in jumbled:
        str=str+letter
    return str


def unshuffle():
    with open("data.clx","r") as infile:
        data=json.load(infile)
    infile.close()
    with open("input.txt","r") as textfile:
        inp=textfile.read()
    inp=inp.split("\n")
    wordlist=[]
    for jumbled in inp:
      hash=process(jumbled)
      try:
          word=data[hash]
      except(KeyError):
          print("No matching word for ",jumbled)
          continue
      wordlist.append(word)
    result="("
    first=1
    for word in wordlist:
        if first:
            first=0
        else:
                result+=","
        result+=word
    result+=")"
    print(result)
        

if __name__ == '__main__':
    unshuffle()
