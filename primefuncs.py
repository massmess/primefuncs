import math

def factorize(n):
	'''Check out all the prime factors of a given number.'''

	limit = int(math.sqrt(n))  # negativity flagged, if any
	primes = []
	k = 6

	# trivial case(s)
	if n == 0 or n == 1:
		return primes

	c = 0
	while True:
		if not n%2 == 0:
			break
		c = c + 1
		n = n // 2

	if not c == 0:
		primes.append((2, c))
		if n == 1:
			return primes  # only 2, early return

	c = 0
	while True:
		if not n%3 == 0:
			break
		c = c + 1
		n = n // 3

	if not c == 0:
		primes.append((3, c))
		if n == 1:
			return primes  # only 3, early return

	while True:
		# loop with steps of 6

		j = k - 1
		if not j <= limit:
			primes.append((n, 1))  # the largest one
			break

		c = 0
		while True:
			if not n%j == 0:
				break
			c = c + 1
			n = n // j

		if not c == 0:
			primes.append((j, c))
			if n == 1:
				break  # all found already

		j = k + 1
		if not j <= limit:
			primes.append((n, 1))  # the largest one
			break
	
		c = 0
		while True:
			if not n%j == 0:
				break
			c = c + 1
			n = n // j
 
		if not c == 0:
			primes.append((j, c))
			if n == 1:
				break  # all found already

		# one small step of 6
		k = k + 6

	# return value, a list
	return primes


def isprime(n):
	'''See if a given number is prime or not.'''

	limit = int(math.sqrt(n))  # negativity flagged, if any
	k = 6
	status = True

	# trivial case(s)
	if n == 0 or n == 1:
		return False

	# not so trivial cases
	if n == 2 or n == 3:
		return True

	if n%2 == 0 or n%3 == 0:
		return False

	while True:
		# loop with steps of 6

		j = k - 1
		if not j <= limit:
			# itself a prime
			break

		if n%j == 0:
			status = False
			break

		j = k + 1
		if not j <= limit:
			# itself a prime
			break

		if n%j == 0:
			status = False
			break

		# one small step of 6
		k = k + 6

	# primality determined
	return status
