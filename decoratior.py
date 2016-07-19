def wrapper(func):
	def dec(*arg):
		return "wrapper for " + func;
	return dec;
@wrapper
def name(myName):
	return myName;



myName = "linchuyuan"
print name(myName);
