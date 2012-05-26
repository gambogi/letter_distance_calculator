# Letter Distance Calculator by zzatkin
import sys

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
first_letter_index = second_letter_index = 0

find_letter = raw_input('Find a letter a certain distance from a specified letter? [y/n] ')

if find_letter == 'y':
	letter = raw_input('Enter the letter [a-z]: ')
	try:
		letter_index = letters.index(letter)
	except:
		quit('Letter not found')
	smallest = abs(letter_index - 25) if abs(letter_index - 25) < 26 else 0
	largest = abs(25 - letter_index) if 0 < abs(25 - letter_index) else 0
	maximum = max([int(smallest),int(largest)])
	distance = raw_input('How far away? [max: '+str(maximum)+']: ')
	try:
		distance = int(distance)
	except:
		quit('Invalid distance')
	if 0 < distance:
		left = letter_index - distance if -1 < letter_index - distance else 0
		right = letter_index + distance if letter_index + distance < 26 else 25
		print ''.join(letters)
		for i in range(0,26):
			if i == left or i == right:
				sys.stdout.write('^')
			else:
				sys.stdout.write(' ')
		sys.stdout.write("\n")
		print 'To the left: '+letters[left]
		print 'To the right: '+letters[right]
	else:
		print 'Distance out of range'
else:
	first_letter = raw_input('Enter first letter [a-z]: ')
	second_letter = raw_input('Enter second letter [a-z]: ')

	for i in range(0,len(letters)):
		if first_letter == letters[i]:
			first_letter_index = i
		if second_letter == letters[i]:
			second_letter_index = i

	if first_letter_index < second_letter_index:
		print 'Distance:' , (second_letter_index - first_letter_index)
	elif second_letter_index < first_letter_index:
		print 'Distance:' , (first_letter_index - second_letter_index)
	else:
		print 'No distance'