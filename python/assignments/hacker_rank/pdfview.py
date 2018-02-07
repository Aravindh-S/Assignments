#!/bin/python3

import sys

def designerPdfViewer(h, word):
    li,pi=[],[]
    for i in word:
        li.append(ord(i)-97)
    
    for i,j in enumerate(h):
        if(i in li):
            pi.append(j)
    print(max(pi)*len(word))
    # Complete this function

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    

