def transform(s):
    		if len(s) % 2 != 0:
        			s1= s[:(len(s)//2)].upper() +s[(len(s)//2):].lower()
        			return s1
    		else:
        			return s
str1="oriJenBeliret"
print("Input : {}\nOutput: {}".format(str1,transform(str1)))
str2="orionmeo"
print("Input : {}\nOutput: {}".format(str2,transform(str2)))
