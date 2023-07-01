
def partition(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i < j:
        while arr[i] <= pivot and i <= high-1:
            i += 1
        while arr[j] > pivot and j >= low+1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def qs(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        qs(arr, low, pivot-1)
        qs(arr, pivot+1, high)


if __name__ == "__main__":
    arr = [4, 6, 2, 5, 7, 9, 1, 3]
    qs(arr, 0, len(arr)-1)
    print(arr)
