from random import shuffle
from datetime import datetime

def insertion_sort(arr : list[int]) -> list[int]:
    result_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > result_arr[-1]:
            result_arr.append(arr[i])
        else:
            for j in range(i):
                if arr[i] < result_arr[j]:
                    result_arr.insert(j, arr[i])
                    break
                else:
                    pass
    return result_arr


LIST_LENGTH = 10000
to_sort = [i for i in range(LIST_LENGTH)]
shuffle(to_sort)
start = datetime.now()
sorted_arr = insertion_sort(to_sort)
elapsedTime = (datetime.now() - start)
print(sorted_arr)

print(f"Sorted: {sorted_arr == sorted(to_sort)}\nTime Taken: {elapsedTime.seconds}s {elapsedTime.microseconds / 1000}ms")