class CounterFile:
	@staticmethod
	def read():
		c_file  = open("counter.txt", "r")
		try:
			n = int(c_file.readline())
		except:
			n = 0
		c_file.close()
		return n

	@staticmethod
	def increment():
		n = CounterFile.read()
		c_file  = open("counter.txt", "w")
		c_file.write(str(n + 1))
		c_file.close()
