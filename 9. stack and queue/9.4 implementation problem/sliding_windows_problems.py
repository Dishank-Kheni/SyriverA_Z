def getMax(arr, k):

    result = []
    for i in range(len(arr)-(k)+1):
        print(arr[i:i+k])
        result.append(max(arr[i:i+k]))

    return result


if __name__ == "__main__":
    print(getMax([4, 0, -1, 3, 5, 3, 6, 8], 3))
