import os
import datetime # just for testingpurpose

start = datetime.datetime.now() # get the starttime

class decodedna:
	def __init__(self,filename):

		
		print("What was his name again?")
		print("Yes, right:")
		realfilname = self.getfilename(filename)
		print(realfilname)
		print("Now we can decode")

		frame = self.readfile(filename)
		print("We are done decoding")
		self.createfile(frame,realfilname)
		print("")
	
	def readfile(self,filename):
		frame = bytearray()		
		inputdir = "inputencoded/%s" % (filename)
		with open(inputdir, "r") as in_file:
			basestr = in_file.read()
			basestr = basestr[384:len(basestr)]
			return self.decode(basestr, frame,0)
				

	def getfilename(self,filename):
		inputdir = "inputencoded/%s" % (filename)
		with open(inputdir, "r") as in_file:
			basestr = in_file.read(384)
			internarray = bytearray()
			realfilename = self.decode( basestr, internarray, 0)
			return (realfilename.decode("utf-8").strip())
				
	def decode(self, basestr, frame, i): # i is needte to find the last base
		retrive = {"AC":0,"CG":0,"GT":0,"TA":0,
				   "AG":1,"CT":1,"GA":1,"TC":1,
				   "AT":2,"CA":2,"GC":2,"TG":2}
		last = basestr[0:1] #first base
		c = 0 # every trimer has 6 values
		byteint = 0 #the actual encodet byte

		for base in basestr:
	#erster buchstabe und zeilenumbruch wird ignoriert
			if( i > 0 and base != "\n"):
				dimer = last + base
				value = retrive[dimer]
				last = base
				if(c < 6):
					byteint = byteint + value*(3**c)
					c = c + 1
				else:
					byteint = value*(3**0)					
					c       = 1
				#ausgabe des int					
				if(c == 6):
					frame.append(byteint)
			i = i + 1
		return frame

	def createfile(self,frame,filename):
		outputdir = "output/%s" % (filename)
		with open(outputdir, "wb") as out_file:
			out_file.write(frame)


for files in os.listdir("inputencoded"):
	decodedna(files)



print("")
stop = datetime.datetime.now()
seconds = stop-start  
print("Job took that long:")
print(seconds)
print("")

