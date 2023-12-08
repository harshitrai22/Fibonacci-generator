def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


number = int(input("Enter How many Fibonacci no. you want"))

if number < 0:
	print("Not valid input")


print("Fibonacci no. in the given range is ")

for i in range(0, number):
	print(fibonacci(i))