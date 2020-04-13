# Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.

def is_prime(dividend):
	if dividend < 2:
		return False
		
	for divisor in range(2, dividend):
		if dividend % divisor == 0:
			return False

	return True

for i in range(10):
    print(f"{i} is a prime number? {is_prime(i)}")
