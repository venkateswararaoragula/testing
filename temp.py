#!/usr/bin/python
list=['a','b','c','d','e','f']
char=raw_input("provide char to insert:")
pos=raw_input("give position of new char:")
def fun1(a,b):
	check = len(list)
	print check,b,a
	if check > b:
		print "can plug in value"
		list[b] = a
	else:print "can't plug in value"
	return list
fun1(char,pos)
