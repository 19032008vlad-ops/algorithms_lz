import random

def bubble_sort_desc(arr):
    a = arr.copy()
    n = len(a)
    comparisons = 0

    print("\n Bublle Sort:")

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

        print(f"Itaration {i + 1}: {a}")

    return a, comparisons


def selection_sort_desc(arr):
    a = arr.copy()
    n = len(a)
    comparisons = 0

    print("\nSelection Sort")

    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] > a[max_idx]:
                max_idx = j

        if max_idx != i:
            a[i], a[max_idx] = a[max_idx], a[i]

        print(f"Iteration {i + 1}: {a}")

    return a, comparisons


def main():

    arr = [random.randint(0, 1000000) for _ in range(100)]

    print("Original list:")
    print(arr)

    bubble_result, bubble_comparisons = bubble_sort_desc(arr)

    selection_result, selection_comparisons = selection_sort_desc(arr)
    
    print("\nResult of bubble sort: ")
    print(bubble_result)

    print("\nResult of selection sort:")
    print(selection_result)

    print("\nNumbers of iteration:")
    print(f"  Bubble sort: {bubble_comparisons}")
    print(f"  Selection sort:   {selection_comparisons}")


    main()