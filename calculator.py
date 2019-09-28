from a import *
from b import * 
from multiply import *
from division import *
def calculator():
	a=23
	b=12
	print("enter 1 for addition,2 for subtraction,3 for multiplication and 4 for division")
	c=2
	if(c==1):
		print(add(a,b))
	elif(c==2):
		print(sub(a,b))
	elif(c==3):
		print(mult(a,b))
	else:
		print(division(a,b))
calculator()

