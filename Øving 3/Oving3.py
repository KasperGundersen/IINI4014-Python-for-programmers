# Creates a emty list for the prime numbers, and the startnumber which in this case is 1
primeNumbers = []
num = 1

# Runs the while-loop until we got 1000 prime numbers
while len(primeNumbers) < 1000:
    # Checks if the number is grater than 1, because prime numbers are natural numbers
    if num > 1:
        # Checks if the number got factors
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            # If the number is a prime number, we add it to the list
            primeNumbers.append(num)
    num += 1

print(primeNumbers)