#
#	Version 0.0.1 beta		Yafet Getachew 5/2014
#
#	Docupy.py is a python script that helps you with the daunting task
#	of documenting your code.
#
#	Don't worry about documentation just give detailed descriptions in 
#	your comments and docupy.py will generate an html based documentation
#	in seconds. But don't forget to use the docupy keywords!!! ->
#	
#	c:\> path\to\docupy\docupy.py -g project_root language
#
# 	language is optional but recommended, -g is for generate and -h is for help
#	
#	~docupy.c (class) also 				~.c
# 	~docupy.f (function)				~.f
#	~docupy.i (interface)				~.i
#	~docupy.a (abstract class)			~.a
#
# 										
#		an example for a c++ function 
#
#		//~dy.f This function calculates the amount of foo in the universe
#
#		int foo(){
#			int foo_amount;
#			//Some code to calculate foo_amount!!
#			return foo_amount;
#		}
#
#

import sys
import string

def init():
	if(len(sys.argv) <= 1):
		print("Looks like you forgot some arguments!")
	else:
		if(sys.argv[1] == "-h"):
			print("I should display some help...") 
		else:
			if(sys.argv[1] == "-g"):
				print("start generating the doc")
			else:
				print("what is that?!");


init() #This is where the magic starts
