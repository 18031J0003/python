
s = input("Enter a String  ")
s1="aeiou"
a=len(s)
c = 0
for k in range(a):
	if(s[k] in s1):
		c+=1
print(c)