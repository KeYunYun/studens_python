# coding: utf-8
import jieba
import jieba.posseg as pseg
import jieba.analyse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def text():
    jieba.load_userdict("userdict.txt")
    jieba.add_word('李铁军')
    test_sent="李小福和李铁军是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    woeds = pseg.cut(test_sent)
    #print(' '.join(woeds))
    for w in woeds:
        print(w.word,w.flag)
    # for x,w in jieba.analyse.extract_tags(test_sent,withWeight=True):
    #     print('%s %s'%(x,w))
    # for x, w in jieba.analyse.textrank(test_sent, withWeight=True):
    #      print('%s %s' % (x, w))

def count(word_dick_name,word_dick_num):
    word=pd.DataFrame({"word_dick_name":word_dick_name,"word_dick_num":word_dick_num})
    print(word.sort_values("word_dick_num",ascending=False))


def main():
    word_lis=[]
    word_dick={}
    word_dick_num=[]
    word_dick_name=[]
    jieba.load_userdict("userdict.txt")
    f=open("news.txt","r")
    fdata=open("data.csv","w")
    line=f.read()

    seg_list=jieba.posseg.cut(line)
    for w in seg_list:
        if "n" in w.flag:
            if len(w.word)>2:
                word_lis.append(w.word)
    # print(word_lis)
    for num in range(len(word_lis)):
        if word_lis[num] in word_dick:
           word_dick[word_lis[num]]+=1
        if word_lis[num] not in word_dick:
            word_dick[word_lis[num]] = 1
    #count(word_dick)
   # print(word_dick)
    for key in word_dick:
        if word_dick[key]>=2:
            word_dick_name.append(key)
            word_dick_num.append(word_dick[key])
            fdata.write(key+","+str(word_dick[key])+"\n")
            # print(key, word_dick[key])
    count(word_dick_name,word_dick_num)

    fdata.close()
    f.close()
    # seg_list=" ".join(seg_list)
    # print(seg_list)
    # for x,w in jieba.analyse.extract_tags(line,withWeight=True):
    #     print('%s %s'%(x,w))
    # f.close()


if __name__ == "__main__":
   main()
   # text()