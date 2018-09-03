import random
start = input('please decide to the start of number of random:  ')
end = input('please decide to the end of number of random:  ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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