import math

def power_mod(base, exponent, modulo):
    result = 1
    base = base % modulo
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulo
        exponent = exponent // 2
        base = (base * base) % modulo
    return result

def count_pairs(N, A, B, M, C, D):
    MOD = 998244353

    def prime_factors_to_dict(prime_factors):
        factors = {}
        for i in range(len(prime_factors)):
            if prime_factors[i] in factors:
                factors[prime_factors[i]] += 1
            else:
                factors[prime_factors[i]] = 1
        return factors

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    x_factors = prime_factors_to_dict(A)
    y_factors = prime_factors_to_dict(C)

    lcm_x = 1
    gcd_y = 1

    for prime, exp in x_factors.items():
        lcm_x = (lcm_x * power_mod(prime, exp * B[x_factors[prime] - 1], MOD)) % MOD

    for prime, exp in y_factors.items():
        gcd_y = (gcd_y * power_mod(prime, exp * D[y_factors[prime] - 1], MOD)) % MOD

    result = 0

    for i in range(1, int(math.sqrt(lcm_x)) + 1):
        if lcm_x % i == 0:
            factor1 = i
            factor2 = lcm_x // i

            # if lcm(factor1, gcd_y) == 1:
            #     result += 1

            if factor1 != factor2 and lcm(factor2, gcd_y) == 1:
                result += 1

    return result % MOD

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
D = list(map(int, input().split()))

result = count_pairs(N, A, B, M, C, D)
print(result)