
s = input("Enter a String  ")
s1="bob"
a=len(s)
b=len(s)
c = 0
for k in range(b-a):
	if(s[k]==s1[0] and s[k]==s1[1] and s[k]==s1[2]):
		k+=1
		c+=1
print(c)