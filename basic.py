def primes(n=1000000):  # generates primes up to n
    m = n + 1
    # numbers = [True for i in range(m)]
    numbers = [True] * m  # EDIT: faster
    for i in range(4, m + 1, 2):
        numbers[i] = False
    for i in range(3, int(n ** 0.5 + 1)):
        if numbers[i]:
            for j in range(i * i, m, 2 * i):
                numbers[j] = False
    primes = [2]
    for i in range(3, m, 2):
        if numbers[i]:
            primes.append(i)
    return (primes)


def miller(n):  # primality test improving fermat
    witnesses = [2, 3, 5, 7, 11]
    if n == 1:
        return (False)
    elif n in witnesses:
        return (True)
    elif n % 2 == 0:
        if n == 2:
            return (True)
        else:
            return (False)
    d = (n - 1) // 2
    s = 1
    while not (d % 2):
        d //= 2
        s += 1
    for witness in witnesses:
        mod = pow(witness, d, n)
        if (mod == 1) ^ (mod == n - 1):
            continue
        for x in range(s - 1):
            mod = (mod * mod) % n
            if mod == n - 1:
                break
        else:
            return (False)
    return (True)


primes = primes(10 ** 6)
length = len(primes)
count = 0


failures = []

for i in range(length - 1):
    pi = primes[i]
    pj = primes[i + 1]
    pk = pj ** 2 - pi ** 2
    if not (miller(pk + pi) or miller(pk + pj) or miller(pk - pi) or miller(pk - pj)):
        count += 1
        # print(pi,pj)
print(count / length)
