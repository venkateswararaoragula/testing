#!/usr/bin/python
print """
1.Telugu
2.English
3.Hindi
4.Maths
5.Science
6.Quit
"""
while True:
	i = raw_input("Choose subject:")
        if i is '1':
		print "Telugu selected"
		print "select right option to exit"
		continue
	elif i is '2':
		print "English selected"
		print "select right option to exit"
		continue
	elif i is '3':
		print "Hindi selected"
		print "select right option to exit"
		continue
	elif i is '4':
		print "Maths selected"
		print "select right option to exit"
		continue
	elif i is '5':
		print "Science selected"
		print "select right option to exit"
		continue
	else: break
print "correct signal passed"

	

#print i
#if i is '6': 
#	print "wrong entry"
#	continue
#if i is '1': print "You selected Telugu"
#elif i == '2': print "you selected English"
#else: print "wrong entry"

#print "end"
