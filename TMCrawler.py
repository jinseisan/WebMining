import requests
import re
import time

#天猫评论爬虫
'''参考博客 https://blog.csdn.net/r3ee9y2oefcu40/article/details/79887474 '''

# 创建循环链接

urls = []

for i in list(range(1,13)):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=527104293077&spuId=472789059&sellerId=2176847013&order=3&currentPage='+str(i)+'&tagId=260&posi=-1'
    urls.append(url)
    #print(url)

# 构建字段容器

nickname = []

ratedate = []

color = []

size = []

ratecontent = []

# 循环抓取数据

i = 1
for url in urls:
    content = requests.get(url).text
    time.sleep(1.1)
    print("正在获取"+ str(i) +"页数据……")
    i += 1

    # 借助正则表达式使用findall进行匹配查询

    nickname.extend(re.findall('"displayUserNick":"(.*?)"',content))

    #color.extend(re.findall(re.compile('颜色分类:(.*?);'),content))

    #size.extend(re.findall(re.compile('尺码:(.*?);'),content))

    ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","fromMall"'),content))

    #ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'),content))


#print(nickname)

# 写入数据

file =open('n_review5.csv','w',encoding='gb18030')
file.write('content\n')

for i in list(range(0,len(nickname))):

    #print("正在写入"+nickname[i]+"的评论……")
    cont = ratecontent[i]+'\n'
    file.write(cont)
    #','.join((nickname[i],ratedate[i],color[i],size[i],

print("写入完毕！")
file.close()