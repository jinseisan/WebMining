from gensim.models import word2vec
import gensim

#特征值(Features)计算

#特征维数
dimension = 50

#导入model
model = word2vec.Word2Vec.load('w2v'+str(dimension)+'.model')

#打开文件
infile = open('分词.csv','r',encoding='utf-8')
outfile = open(str(dimension)+'features.csv','w',encoding='utf-8')

#第一行标题写入
for i in range(1,dimension+1):
    outfile.write(str(i) + ',')
outfile.write('class\n')

#构建评论数组
content = infile.read().split('\n')

for i in list(range(0,len(content))):
    print('正在计算第'+str(i+1)+'条评论特征值……')
    feature = [0] * dimension
    #获取词数组
    words = content[i].strip(' ').split(' ')
    #有效词数计数
    count = len(words)
    #循环求和
    for word in words:
        if(model.__contains__(word)):
            feature += model[word]
        else:
            count -= 1
    #求均值
    feature = feature/count
    for f in feature:
        outfile.write(str(f) + ',')
    #情感标注：前1500条是正向，后1500条是负向
    if(i < 1500): outfile.write('1\n')
    else: outfile.write('-1\n')

#关闭文件
infile.close()
outfile.close()
