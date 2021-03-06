from primefuncs import isprime

print(isprime.__doc__)
print("-- Type 'QUIT' to end the test.")

while True:
	s = input("-- Enter a number for the test: ")

	if s.upper() == 'QUIT':
		print("Done.")
		break

	try:
		n = int(s)
	except ValueError:
		print("Wrong number (or not one)! Try again!")
		continue

	if n <= 0:
		print("Number must be non-zero, non-negative!")
	else:
		print("Checking...")
		print(f"To be tested: {n}")
		if isprime(n):
			print(f"(O) {n} is a PRIME NUMBER.")
		else:
			print(f"(X) {n} is NOT a prime number.")
