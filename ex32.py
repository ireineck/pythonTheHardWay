# loops and lists

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'aprocots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count: 
	print "this is count %d" % number

for fruit in fruits:
	print "%s \n" % fruit

for i in change: 
	print "I got %r" % i

elements = []

for i in range (0, 6):
	print "adding %d to the list" % i
	# append is a function that lists understand
	elements.append(i)

for i in elements:
	print "Element was: %d" % i