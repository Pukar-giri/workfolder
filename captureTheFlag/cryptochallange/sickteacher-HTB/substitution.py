#!/usr/bin/pythonc
import operator
import re
import string
from matplotlib import pyplot as plt

key={}
substitutable=string.ascii_uppercase.split()
def substitute(cipher,key):
    result=""
    for letter in cipher:
        if (letter in string.ascii_uppercase):
            result=result+key[letter]
        else:
            result=result+letter
    print(result)

def keylen(elem):
    return len(elem[0])

def breakdown(cipher):
    ret={}
    cwords=re.split(r'\s',cipher)
    for cword in cwords:
        count=0
        index=-1
        for cword1 in cwords:
            index=index+1
            if cword1==cword:
                count=count+1
                del cwords[index]
        ret.update({cword:count})
    ret={key:value for key,value in sorted(ret.items(),key=keylen)}
    final=[]
    keys=[(key,freq) for key,freq in ret.items()]
    for (key,freq) in keys:
        samelength={}
        index=-1
        tobedeleted=[]
        for (word,frequency) in keys:
                index=index+1
                if len(key)==len(word):
                        samelength.update({word:frequency})
                        tobedeleted.append(index)
        tobedeleted.reverse()
        for index in tobedeleted:
                del keys[index]
        samelength={key:value for key,value in sorted(samelength.items(),key=operator.itemgetter(1),reverse=True)}                
        final.append(samelength)
    return(final)
def solve(cipher):
    digestwords=breakdown(cipher)
    words=[]
    for dicti in digestwords:
        word=[key for key,value in dicti.items()]
        words.append(word)
    print(words)





if __name__=="__main__":
    sorted_letters_real = ["E", "A", "R", "I", "O", "T", "N", "S", "L", "C", "U", "D", "P", "M", "H", "G", "B", "F","Y", "W", "K", "V", "X", "Z", "J", "Q"]
    cipher="""KBJICYP CZ KHLTIKWECD

KHLTIKWECD RWMI GBQW JCNW IBNW BM NHP CZ 2017. JBMLW IKWM, BI KHJ FYCRM QWYP VOBLTGP IC IKCOJHMSJ CZ NWNEWYJ ZYCN HGG CQWY IKW FGCEW.
IKW KHGG CZ ZHNW GBJIJ IKW ICA 100 OJWYJ BM CYSWY CZ ACBMIJ. HI IKW IBNW CZ RYBIBMF, IKW ICA 3 OJWYJ HYW JIWZHMC118, ZBGGBACJ HMS HKNWS.
IKWYW HYW JCNW ZCYONJ, H JKCOIECD HMS H JGHLT LKHMMWG. JGHLT HMS JKCOIECD HYW HRWJCNW, EOI IKW ZCYONJ MWWS JCNW GCQW! B RBJK NCYW AWCAGW OJWS IKWN.
KCAWZOGGP IKBJ BJ WMCOFK IWDI IC KWGA RBIK PCOY JOEJIBIOIBCM! FWI LYHLTBM! AJ SCM'I ZCYFWI IC JOAACYI KHLTIKWECD BZ PCO LHM JAHYW JCNW NCMWP. WQWYP AWMMP KWGAJ!

DCDC - HYYWDWG
ZGHF GCYWNBAJONSCGCYJBIHNWI"""
    sorted_letters_here= sorted(string.ascii_uppercase, key=lambda letter, cipher=cipher: len([c for c in cipher if c == letter]),reverse=True)
    key=dict(zip(sorted_letters_here,sorted_letters_real))
    print(key)
    solve(cipher)
    substitute(cipher,key)
