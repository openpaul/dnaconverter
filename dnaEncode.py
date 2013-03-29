import os

class encodedna:
	def __init__(self, filename):
		hugetryte = list()
		print("Initiate reading")
		hugetryte = self.readfile(filename,hugetryte)
		print("File has been readen")
		self.converttryte2DNA(filename,hugetryte)
		print("We are done")

########################################################
# this opens any file and reads its bytes
	def readfile(self,filename,hugetryte):
	
		#open file trough path in binary mode "rb"
		filepath = "input/%s" % (filename)
		with open(filepath, "rb") as in_file:

			#load the bytes into array
			myfilearray = in_file.read()

			#loop over the array of bytes
			for item in myfilearray:
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
		next = {"A0":"G",
		"A1":"C",
		"A2":"T",
		"G0":"C",
		"G1":"T",
		"G2":"A",
		"C0":"T",
		"C1":"A",
		"C2":"G",
		"T0":"A",
		"T1":"G",
		"T2":"C"}		
		last = "A"
		outputdir = "inputencoded/%s" % (filename)
		with open(outputdir, "w") as out_file:
			out_file.write("A"); #The first letter has to be an A, by convention
		with open(outputdir, "a") as out_file:		
			for n in hugetryte:
				dimer  = "%s%s" % (last,n)
				last   = next[dimer]
				#DNA  = "%s%s" % (DNA, last)
				out_file.write(last);

#encodedna()

#os.chdir("input")
for files in os.listdir("input"):
	encodedna(files)

