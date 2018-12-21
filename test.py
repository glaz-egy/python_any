import MeCab
from random import choice

def DataCreate(text, mecab):
    text = text.strip()
    print(text)
    if text == '\n': return
    raw = mecab.parse(text)
    raw = raw.strip().split('\n')
    datalist = []
    for data in raw:
        datalist.append(data.split('\t')[0])
    datalist.remove('EOS')
    returnlist = []
    for i in range(len(datalist)):
        returnlist.append(['BOS' if i == 0 else datalist[i-1], datalist[i], datalist[i+1] if i+1 < len(datalist) else 'EOS'])
    return returnlist

def Markov(datalist):
    nextstring = next(datalist, ['BOS'], Start=True)
    out = nextstring[0]
    while True:
        if nextstring[1] == 'EOS': return out
        out += nextstring[1]
        nextstring = next(datalist, nextstring)
        if len(out) > 140:
            nextstring = next(datalist, ['BOS'], Start=True)
            out = nextstring[0] + nextstring[1]

def next(datalist, s, Start=False):
    if Start: nextlist = [data for data in datalist if data[0] == s[0]]
    else: nextlist = [data for data in datalist if data[0] == s[0] and data[1] == s[1]]
    ch = choice(nextlist)
    print(ch)
    return [ch[1], ch[2]]

if __name__=='__main__':
    with open('textdata.txt', 'r', encoding='utf-8') as f:
        textdata = f.readlines()
    datalist = []
    mecab = MeCab.Tagger()
    for text in textdata:
        datalist.extend(DataCreate(text, mecab))
    print(datalist)
    while True:
        i = input()
        if i == 'e': break
        else: print(Markov(datalist))