data = []
with open ("reviews.txt", "r") as a:
    for comet in a:
        data.append(comet)
wc = {}
for word in data:
    w = word.split()#用預設值多空自動去掉
    for word in w:
        if word in wc:
            wc[word]+=1
        elif word not in wc:
            wc[word] = 1
a = 0
for word in wc:
    if a < wc[word]:
        a = wc[word]
        b = word
    else:
        continue
r = []
for word in wc:
    if wc[word] == a:
        r.append(word)
print(r)
print(a, b)
while True:
    key_words = input("keywords: ")
    if key_words not in wc:
        print("Wrong!")
    elif key_words == "q":
        break
    else:
        print(key_words, ":", wc[key_words])




