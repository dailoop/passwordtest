import random
start = input("輸入起始數字: ")
end = input("輸入結束數字: ")
start = int(start)
end = int(end)
r = random.randint(start, end)
y = 0
while True:
	x = input("請輸入數字: ")
	if int(x) == r:
		y += 1
		print("恭喜答對! 這是第 ", y, "次")
		break
	elif int(x) != r:
		y += 1
		if int(x) > r:
			print("錯誤,請在往小的猜")
		elif int(x) < r:
			print("錯誤,請在往大的猜")
	print("這是第", y, "次")