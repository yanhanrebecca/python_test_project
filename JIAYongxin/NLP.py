import jieba
from gensim import corpora, models
from gensim.models import LdaModel

# 添加停用词表
stop_words = set(['和', '是', '一种', '一些'])

# 示例文本数据
documents = ["我喜欢吃苹果和香蕉",
             "今天天气晴朗，适合出去玩",
             "苹果是一种水果",
             "我不喜欢下雨天",
             "我今天买了一些水果回家，包括苹果和香蕉"]

# 分词并去除停用词
texts = [[word for word in jieba.cut(document) if word not in stop_words] for document in documents]

# 构建词典
dictionary = corpora.Dictionary(texts)

# 基于词典将文本转换为词袋表示
corpus = [dictionary.doc2bow(text) for text in texts]

# 训练LDA模型
lda_model = models.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=20)

# 输出每个主题的词分布
for i, topic in lda_model.print_topics(num_words=3):
    print("Topic {}: {}".format(i, topic))

# 使用模型推断新文档的主题分布
new_document = "我今天买了一些水果回家"
new_bow = dictionary.doc2bow(jieba.lcut(new_document))
print("新文档的主题分布：", lda_model.get_document_topics(new_bow))
