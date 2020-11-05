# Assignment 6
### Due date: September 30, 2020 6:19 PM

---

# RSA public-key cryptography
## Introduction
In this assignment we will look into the details of the RSA encryption algorithm and try to decrypt a short message.

Read the [RSA Wikipedia page](https://en.wikipedia.org/wiki/Rsa_encryption). To suppliment your understanding, here are a few other resources:

- [RSA Algorithm](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/)
- [RSA implementation](https://gist.github.com/JonCooperWorks/5314103)

RSA has its share of weaknesses, most notably to do with key length. Read about previous attacks on RSA:

- [Brute force attacks on cryptographic keys](https://www.cl.cam.ac.uk/~rnc1/brute.html)
- [Cracking Crypto Keys on the NOW Cluster](http://www.isaac.cs.berkeley.edu/isaac/crypto-challenge.html)

In this assignment, you won't need a powerful computer. The implementation of RSA used here is a toy example. The second link above mentions that there is some known plaintext provided as part of the challenge. This lets you know when you have found the right key. Typically this information is not available!

### Running the RSA example
1. Install [NumPy](http://www.numpy.org/). For example, on a Debian Linux system, execute the following command: `sudo apt install python-numpy` or for Python 3 `sudo apt install python3-numpy`.
2. The code rsa.py is attached. 
3. Run the code with a message to encrypt:

`$ python rsa.py "This is a secret message."`
Output:
`('Public key: ', (41563, 65383))
('Private key: ', (19027, 65383))
Your encrypted message is:
[50786L, 62544L, 29219L, 24566L, 11357L, 29219L, 24566L, 11357L, 14356L, 11357L, 24566L, 21068L, 29476L, 52833L, 21068L, 27065L, 11357L, 45100L, 21068L, 24566L, 24566L, 14356L, 44077L, 21068L, 62287L]
Your message is:
This is a secret message.`

The code takes a plaintext message, generates a public-private keypair, and encrypts the message using the public key. Then, the message is decrypted using the private key.

### Task description
Study the code in rsa.py. Your task in this assignment is to uncover the private key and recover the plaintext from the encrypted message. In order to help with this challenge, you are also given a short piece of the plaintext to use as a way to filter valid results.

You are given the public key and a snippet of the plaintext. Using only this information, recover the private key used to encrypt the message.

Public key:
`(29815, 100127)`

Plaintext snippet in Python code for a candidate decrypted message m (should evaluate to True):

`m.startswith("h")`
Encrypted message (ciphertext):
`[84620L, 66174L, 66174L, 5926L, 9175L, 87925L, 54744L, 54744L, 65916L, 79243L, 39613L, 9932L, 70186L, 85020L, 70186L, 5926L, 65916L, 72060L, 70186L, 21706L, 39613L, 11245L, 34694L, 13934L, 54744L, 9932L, 70186L, 85020L, 70186L, 54744L, 81444L, 32170L, 53121L, 81327L, 82327L, 92023L, 34694L, 54896L, 5926L, 66174L, 11245L, 9175L, 54896L, 9175L, 66174L, 65916L, 43579L, 64029L, 34496L, 53121L, 66174L, 66174L, 21706L, 92023L, 85020L, 9175L, 81327L, 21706L, 13934L, 21706L, 70186L, 79243L, 9175L, 66174L, 81327L, 5926L, 74450L, 21706L, 70186L, 79243L, 81327L, 81444L, 32170L, 53121L]`

Encrypted message (ciphertext) without 'L' in case your version of Python complains:

`[84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]`
### Hints
- You will likely encounter the exception `ValueError: chr() arg not in range(256)`. This means the value passed to the chr() function in decrypt() is out of range. Use a `try-except` block to surround this call and `pass` on this exception. Since we know that our message is text (assume just ASCII text), any messages with characters outside of the byte range (0-255) can be excluded, even more if you study the ASCII table a little more closely. Read more about [Exception handling in Python](https://wiki.python.org/moin/HandlingExceptions).
- You may notice that an algorithm for generating prime numbers from Assignment 3 is included in the file! Look at how these primes are used.

### Submission
Submission consists of two things:

1. The full plaintext (decrypted message).
2. **A paragraph of text detailing:**
    1. A description of how you approached the problem.
    2. What are the problems with this simple implementation of RSA?
    3. Did you find multiple solutions? Explain.

No code is required to be submitted.
