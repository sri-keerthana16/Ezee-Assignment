def convert(input1):
    		input1= ''.join(char for char in input1 if not char.isdigit())
   		input1 = ''.join([' ' if not char.isalnum() else char for char in input1])
    		return input1
input1 = "Hello User!123@LaL Check out this Game"
print(" Input : {} \n Output : {}".format(input1,convert(input1)))
