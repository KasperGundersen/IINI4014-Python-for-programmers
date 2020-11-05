# Assignment 3
### Due date: September 9, 2020 11:59 PM


---
##Finding prime numbers
**Introduction**
A prime number is defined as any integer that is only evenly divisible by 1 and itself. Prime numbers have been studied for thousdands of years, but the method for generating prime numbers has not changed much during this time; it still takes a lot of computational effort to find them.

The problem of finding prime numbers is actually a benefit to the robustness of modern cryptography. In some public key cryptography schemes such as RSA, a public key consists of the product of two large prime numbers. These two prime numbers are secret, and make up the private key. It is computationally infeasable (i.e., it could take thousands of years) to factor the public key to find the primes that make up the private key, and so any message encrypted with the private key is safe.

The Wikipedia page on prime numbers provides an interesting overview of the history of this topic.

##Assignment
Write code that prints out the first 1000 prime numbers. The code must calculate the prime numbers; you are not allowed to use a table of pre-calculated primes.

Hint: A naive method would check that a given number is divisible by all smaller numbers. Can you find a more efficient way?

Aim to write code that is fast!
