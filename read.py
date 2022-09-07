data = []
x = 0
y = 0
c = 0
with open ("reviews.txt", "r") as a:
    for comet in a:
        data.append(comet)
        y += len(comet)
        x += 1
        if x % 1000 == 0:
            print(len(data))
        if len(comet) < 100:
            c += 1
    print("留言平均長度", y/len(data))
    print("有", c, "筆資料長度小於100")
print("讀取玩了", "總共有", len(data), "筆")

new = []
for i in data:
    if len(i) < 100:
        new.append(i)
print(len(new))
print(len(new[2]))


new1 = []
for r in data:
    if "good" in r:
        new1.append(r)
print(len(new1))
print(new1[4])


new2 = ["sexy" for d in data if "sexy" in d]
print(len(new2))

new4 = ["sexy" in d for d in data]
print(new4)