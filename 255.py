dnaint = 255
rest   = 255
i      = 6 #number of iterations
ternary = list()
while i > 0:
	number = dnaint//3
	rest   = dnaint%3
	dnaint = number
	i      = i - 1 # next iteration
	ternary.append(rest)
	#print(rest)
print(ternary)


#

# conversion from DNA
retrive = {"AG":0,"GC":0,"CT":0,"TA":0,
		   "AC":1,"GT":1,"CA":1,"TG":1,
		   "AT":2,"GA":2,"CG":2,"TC":2}

data = "AGTGCTGCTATCT"
011001 0
					
