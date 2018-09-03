import random

r = random.randint(1,100)
while True:
	num = input('plase guess number:')
	num = int(num)
	if num == r:
		print('Correct')
		break
	elif num > r:
		print(' Answer is more than number')
	elif num < r:
		print(' Answer is less than number')