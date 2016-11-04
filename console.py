#!/usr/bin/python
while True:
	print """
	1.Telugu
	2.English
	3.Hindi
	4.Maths
	5.Science
	6.Quit
	"""
	i = raw_input("Choose subject:")
        if i.isdigit():
		if i >= 6 or i <= 0:
			print i
			print "wrong selection"
			break
		elif i == 1:
			print "Telugu selected"
			print "select right option to exit"
		elif i == 2:
			print "English selected"
			print "select right option to exit"
		elif i == 3:
			print "Hindi selected"
			print "select right option to exit"
		elif i == 4:
			print "Maths selected"
			print "select right option to exit"
		elif i == 5: 
			print "Science selected"
			print "select right option to exit"
print "you choose right option to exit"
