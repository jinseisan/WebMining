#coding=gb18030
import jieba
import jieba.posseg as psg

#�ִ�

file =open('resources/��è����.csv','r',encoding='gb18030')
outfile = open('resources/�ִ�.csv','w',encoding='gb18030')

#���˵��Ĵ��Ժ�Ľ��
txtlist=[]

#���б�Ϊ�Լ�����Ҫ���˵��Ĵ���
cx=["x","w","t"]

#�����û��ʵ�
jieba.load_userdict('userdic.txt')

#�����ĵ�
str1 = file.read()
#���д��д��Եķִ�
cut = psg.cut(str1)
#���Թ��˲�д���ĵ�
for pair in cut:
    if pair.word == '\n':
        outfile.write('\n')
    elif pair.flag not in cx:
        txtlist.append(pair.word)
        outfile.write(pair.word + ' ')
print(len(txtlist))

file.close()
outfile.close()