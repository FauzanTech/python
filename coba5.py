def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def count_divisible_numbers(N, A, B):
    lcmAB = lcm(A, B)
    count = N // A + N // B - N // lcmAB
    return count


jumlahBilangan, A, B = list(map(int, input().split()))
# result = [i%A == 0 or i%B == 0 for i in range(1, jumlahBilangan+1)]
# print(count_divisible_numbers(jumlahBilangan, A, B))

# print(jumlahBilangan//(A+jumlahBilangan)//(B-jumlahBilangan)//(jumlahBilangan))