def minimum_max_passengers(N, A, D):
    max_passengers = A[0]
    
    for i in range(N - 1):
        max_passengers_to_next = min(max_passengers + D[i], A[i + 1])
        max_passengers = max(max_passengers_to_next, max_passengers)

    # j = 0
    for i in range(1, N):
        j = min(max_passengers + D[i-1], A[i])
        
    return abs(max_passengers - j)

N = int(input())
A = list(map(int, input().split()))
D = list(map(int, input().split()))

hasil = minimum_max_passengers(N, A, D)
print(hasil)