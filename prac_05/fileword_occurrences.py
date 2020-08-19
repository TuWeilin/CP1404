sentence_get = str(input('text: '))
sentence_get = str(sentence_get)
sentence_get = sentence_get.split()
sentence_dic = dict()
for word in sentence_get:
    sub = word
    count = sentence_get.count(sub)
    print(count)
    if word not in sentence_dic:
        sentence_dic[word] = count
print(sentence_dic)