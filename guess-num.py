import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 
	num = input('plase guess number:')
	num = int(num)
	if num == r:
		print('Correct')
		print('This is you guess',count,'times')	
		break
	elif num > r:
		print(' Answer is less than number')
	elif num < r:
		print(' Answer is more than number')
	print('This is you guess',count,'times')