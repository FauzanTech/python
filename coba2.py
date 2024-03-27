jumlah_string, jumlah_operasi = list(map(int, input().split()))
string1 = input()
arr = [list(map(int, input().split())) for i in range(jumlah_operasi)]

string1 = list(string1)

for i in range(jumlah_operasi):
    if arr[i][0] == 1:
        string1[arr[i][1]-1], string1[arr[i][2]-1] = string1[arr[i][2]-1], string1[arr[i][1]-1]   
    else:
        new_list = list("".join(string1)[arr[i][1]-1:arr[i][2]])
        new_list.reverse()
        string1[arr[i][1]-1:arr[i][2]] = "".join(new_list)  

print("".join(string1))
