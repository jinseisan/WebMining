from gensim.models import word2vec
import gensim
import logging

#调用word2vec算法学习获得词向量模型
#注：需要将 分词.csv 文件编码改为utf-8

#控制台显示过程信息
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#特征维数
dimension = 150
#从分词语料构建可处理数据
sentences = word2vec.Text8Corpus('分词.csv')
#模型定义
model = gensim.models.Word2Vec(sentences, sg=1, size=dimension,  window=5,  min_count=5,  negative=3, sample=0.001, hs=1, workers=4)
#model = word2vec.Word2Vec.load('word2vec.model')
print(model)
#保存模型
model.save('w2v'+str(dimension)+'.model')
'''
y = model.most_similar(positive=['看清楚'], topn=10)
for item in y:
    print(item[0],item[1])
'''
