import random

r = random.randint(1, 100)
while True:
	num = input('Try A Number: ')
	num = int(num)
	if num == r:
		print('Congratz, You Are Right!')
		break
	elif num > r:
		print('Sorry, Try A Smaller Number Please.')
	elif num < r:
		print('Sorry, Try A Bigger Number Please')