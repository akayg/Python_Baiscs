#Goal of this tryout is to create a function from scratch and invoke it for the given problem
def convert_fintoc(data1):
	conversion = (data1-32)*(5/9)
	return conversion
tmp=int(input('Enter temp in Fahrenheit'))
temp_inF = convert_fintoc(tmp)
print(temp_inF)