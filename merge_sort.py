def merge_sort(list):
    """
    Mengurutkan list dari terkecil ke terbesar
    """
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    new = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    while i < len(left):
        new.append(left[i])
        i+=1

    while j < len(right):
        new.append(right[j])
        j+=1

    return new

def verified(list):
    if len(list) <= 1:
        return True
    return list[0] <= list[1] and verified(list[1:])
     
arr = [1, 5, 6, 4]
print("Sebelum di sort: ", arr)
print(verified(arr))

arrsorted = merge_sort(arr)
print("Sesudah di sort: ", arrsorted)
print(verified(arrsorted))