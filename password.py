password = "a123456"
x = 3
while x != 0:
	passuser = input("請輸入密碼: ")
	if passuser == password:
		print("登入成功")
		break
	elif passuser != password:
		x = x - 1
		if x != 0:
			print("密碼錯誤!" + "還剩" + str(x) + "機會")
		elif x == 0:
			print("密碼錯誤!" + "沒機會了")