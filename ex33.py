# while loops

i = 0
numbers = []

while i < 6: 
	print "at the top i is %d" % i 
	numbers.append(i)

	i = i + 1
	print "numbers now: ",  numbers # the comma concatinates instead of the '+'

print "The numbers: "

for num in numbers:
	print num