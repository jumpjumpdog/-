#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re,sys




def fileToString(filePath):
    with open(filePath, "r") as f:
        dataString = f.read(100)
        while  not dataString :
            dataString += f.read(100)
    dic = wordCount(dataString)
    sortResult(dic)

def wordCount(dataString):
    words = re.compile(r"([a-zA-Z]+)")
    dic = {}
    for x in words.findall(dataString):
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1

    return dic


def sortResult(dic):
    afterSort = []
    for key, value in  dic.items():
        afterSort.append((key,value))
    afterSort.sort(key=lambda t:t[0])

    with open("result.txt","a+") as f:
        for x in afterSort:
            f.write("{0:5s}{1}{2}{3}".format(x[0],":",x[1],'\n'))










if __name__ == "__main__":
    fileName = sys.argv[1]
    fileToString(fileName)


