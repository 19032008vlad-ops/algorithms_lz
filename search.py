import random

def line_search(arr, target):
    comprations = 0
    for i in range(len(arr)):
       comprations += 1
    if arr[i] == target:
            return i, comprations
    return 0, comprations


def binary_search(arr, target):
    comprations = 0
    left, right = 0, len(arr) - 1

    while left <= right:
       comprations += 1
       mid = (left + right) // 2

    if arr[mid] == target:
            return mid, comprations
    elif arr[mid] < target:
            left = mid + 1
    else:
            right = mid - 1

    return 0, comprations


def create_sorted_unique_list(size, min_val = 0, max_val = 1000000):
    numbers = set()
    while len(numbers) < size:
        numbers.add(random.randint(min_val, max_val))
    return sorted(numbers)


def main():
    
    arr = create_sorted_unique_list(100)

    num = input("Enter a number for search: ").strip()
    target = int(num[0])
    

    print("\nLine search")
    lin_index, lin_comp = line_search(arr, target)
    if lin_index != -1:
        print(f"Element was founded with index: {lin_index}")
    else:
        print("Element wasn't founded ")
    print(f"Comprations: {lin_comp}")


    print("\nBinary search")
    bin_index, bin_comp = binary_search(arr, target)
    if bin_index != -1:
        print(f"Element was founded with index: {bin_index}")
    else:
        print("Element wasn't founded")
    print(f"Comprations: {bin_comp}")

    

    main()