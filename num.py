import random
start = input('请决定随机数字范围开始值')
end =input('请决定随机数字范围结束值')
start = int(start)
end = int(end)

r = random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('请猜数字')
	num = int(num)
	if num == r:
		print('你猜中了')
		print('这是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('这是你猜的第', count, '次')	
