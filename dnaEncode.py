import os
import datetime # just for testingpurpose
version = "Version 0.1 beta"

start = datetime.datetime.now() # get the starttime

class encodedna:
	def __init__(self, filename):
		hugetryte = list() # the list with all the 0,1 and 2's
		
		self.encodeName(filename,hugetryte )
		print('Initiate reading of File "%s"' % (filename))
		hugetryte = self.readfile(filename,hugetryte)
		print("File has been readen")
		print("We will now convert it into DNA")
		self.converttryte2DNA(filename,hugetryte)
		print("We are done")
		#print(hugetryte)


	def encodeName(self, filename,hugetryte ):
		print("first we will encode the filename")
		filename.encode("utf-8")
		#64bit are the filename		
		length = (len(filename))
		missing = 64 - length
		while missing > 0:
			filename = filename + (" ")
			missing = missing -1		
		
		filnemabytes = bytes(filename, 'utf-8')

		hugetryte = self.bytearrayconversion(filnemabytes,hugetryte)
		return hugetryte

########################################################
# this opens any file and reads its bytes
	def readfile(self,filename,hugetryte):
	
		#open file trough path in binary mode "rb"
		filepath = "input/%s" % (filename)
		with open(filepath, "rb") as in_file:

			#load the bytes into array
			myfilearray = in_file.read()
			hugetryte = self.bytearrayconversion(myfilearray,hugetryte)
			return hugetryte
	
	def bytearrayconversion(self,bytearray,hugetryte):
		#loop over the array of bytes
		for item in bytearray:
		#each byte as its integer now needs to be calculatet as ternary number
		# so we divide trough 3 and as our new format will have the base of 3 we will have to make 6 iterations so we can encode numbers until 255
			dnaint = item    # copy the integer
			rest   = dnaint  # the rest by start is the numer
			i      = 6       # the number of iterations
			ternary = list() # ternary is the list we save our "trytes" in
					
			while i > 0:
				rest   = dnaint%3    # the rest is interesting
				dnaint = dnaint//3   # the integer to pass on
				i      = i - 1       # next iteration
				hugetryte.append(rest) # the rest gets saved
		return hugetryte




	def converttryte2DNA(self,filename,hugetryte):
		#global DNA
		next = {"A0":"C",
				"A1":"G",
				"A2":"T",
				"G0":"T",
				"G1":"A",
				"G2":"C",
				"C0":"G",
				"C1":"T",
				"C2":"A",
				"T0":"A",
				"T1":"C",
				"T2":"G"}	
		last = "A"	
		outputdir = "inputencoded/%s.fasta" % (filename)
		with open(outputdir, "w") as out_file:
			out_file.write("A"); #The first letter has to be an A (in this software)
		with open(outputdir, "a") as out_file:		
			for n in hugetryte:
				dimer  = "%s%s" % (last,n)
				last   = next[dimer]
				#DNA  = "%s%s" % (DNA, last)
				out_file.write(last);




print("############################################")
print("# Welcome to DNAConverter %s #" % (version))
print("############################################")
print("It comes with no waranty and no usefull function at all")
print("Read the readme on github to learn how it works:")
print("https://github.com/openpaul/dnaconverter/")
print("")
print("You can modify, fork or mess around with the code as much as you would like to")
print("Just know: Paul S. started it")
print("")
print("")


# loop trough the folder
for files in os.listdir("input"):
	encodedna(files)
	print("")
	print("------")
	print("")



print("")
stop = datetime.datetime.now()
seconds = stop-start  
print("Job took that long:")
print(seconds)
print("")

