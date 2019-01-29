print("Task 2-2")
a = int (input("Enter a value"))
if a % 2 != 0:
	print("Weired")
elif a % 2 == 0 and a >= 2 and a <= 5:
	print("Not weired")
elif a % 2 == 0 and a >= 6 and a <= 20:
	print("weired")
elif a % 2 ==0 and a > 20:
	print("Weired")