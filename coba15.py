N = int(input())
string = [input() for _ in range(N)]

for st in string:
    new = list(st)
    # if new.count("(") > 0 or new.count("[") > 0:
    #     if new.count("(") == new.count(")") and new.count("[") == new.count("]"):
    #         print("iya")
    #     else:
    #         print("tidak")
    print("".join(new))
    new.sort()
    print("".join(new))