def permutation(frequency, ds, arr):

    if len(ds) == len(arr):
        print(ds)
        return

    for i in range(len(arr)):
        if not frequency[i]:
            frequency[i] = True
            ds.append(arr[i])
            permutation(frequency, ds, arr)
            ds.pop()
            frequency[i] = False


if __name__ == "__main__":
    arr = [1, 2, 3]
    frequency = [False for _ in range(len(arr))]
    permutation(frequency, [], arr)
