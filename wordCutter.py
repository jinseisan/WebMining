#coding=gb18030
import jieba
import jieba.posseg as psg

#分词

file =open('resources/天猫评价.csv','r',encoding='gb18030')
outfile = open('resources/分词.csv','w',encoding='gb18030')

#过滤掉的词性后的结果
txtlist=[]

#词列表为自己定义要过滤掉的词性
cx=["x","w","t"]

#导入用户词典
jieba.load_userdict('userdic.txt')

#读入文档
str1 = file.read()
#进行带有词性的分词
cut = psg.cut(str1)
#词性过滤并写入文档
for pair in cut:
    if pair.word == '\n':
        outfile.write('\n')
    elif pair.flag not in cx:
        txtlist.append(pair.word)
        outfile.write(pair.word + ' ')
print(len(txtlist))

file.close()
outfile.close()