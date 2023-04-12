import nltk
from nltk.corpus import wordnet

# 定义要查询的单词
word = "dog"

# 打印该单词的所有同义词
synonyms = []
for syn in wordnet.synsets(word):
    print(syn, syn.lemmas())
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print("Synonyms of", word + ":", set(synonyms))

# # 打印该单词的所有反义词
# antonyms = []
# for syn in wordnet.synsets(word):
#     for lemma in syn.lemmas():
#         if lemma.antonyms():
#             antonyms.append(lemma.antonyms()[0].name())
# print("Antonyms of", word + ":", set(antonyms))

# # 打印该单词的上位词和下位词
# hypernyms = []
# hyponyms = []
# for syn in wordnet.synsets(word):
#     for hypernym in syn.hypernyms():
#         for lemma in hypernym.lemmas():
#             hypernyms.append(lemma.name())
#     for hyponym in syn.hyponyms():
#         for lemma in hyponym.lemmas():
#             hyponyms.append(lemma.name())
# print("Hypernyms of", word + ":", set(hypernyms))
# print("Hyponyms of", word + ":", set(hyponyms))

# # 打印该单词的部分和整体
# meronyms = []
# holonyms = []
# for syn in wordnet.synsets(word):
#     for part in syn.part_meronyms():
#         for lemma in part.lemmas():
#             meronyms.append(lemma.name())
#     for whole in syn.substance_holonyms():
#         for lemma in whole.lemmas():
#             holonyms.append(lemma.name())
# print("Meronyms of", word + ":", set(meronyms))
# print("Holonyms of", word + ":", set(holonyms))

# # 打印该单词的属性
# attributes = []
# for syn in wordnet.synsets(word):
#     for attr in syn.attributes():
#         for lemma in attr.lemmas():
#             attributes.append(lemma.name())
# print("Attributes of", word + ":", set(attributes))

# # 打印该单词的词汇链关系
# troponyms = []
# for syn in wordnet.synsets(word):
#     for troponym in syn.entailments():
#         for lemma in troponym.lemmas():
#             troponyms.append(lemma.name())
# print("Troponyms of", word + ":", set(troponyms))
