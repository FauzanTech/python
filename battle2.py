jumlah_bilangan = int(input())
bilangan = list(map(lambda x: abs(int(x)),input().split()))
print(min(bilangan))