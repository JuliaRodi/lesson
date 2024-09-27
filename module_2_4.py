numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
in_primes = []
in_not_prime = []
for i in numbers:
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            in_not_prime.append(i)
            break
    if i not in in_not_prime:
            in_primes.append(i)
in_primes.remove(1)
print("Primes",in_primes)
print("Not_prime", in_not_prime)
