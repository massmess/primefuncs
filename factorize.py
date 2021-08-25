from primefuncs import factorize

print(factorize.__doc__)
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
    print("Finding...")
    y = factorize(n)
    print(f"To be tested: {n}")
    print("Its prime factor(s):")
    print(y)
    if len(y) == 1:
      if y[0][1] == 1:
        assert y[0][0] == n, "Something goes wrong!"
        print(f"** {n} is a PRIME NUMBER!")
