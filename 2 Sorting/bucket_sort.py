def bucketSort():

    arr = [7, 500, 26, 6, 668, 578, 45, 28, 3974, 175]

    bucket = [[] for _ in range(len(str(max(arr))))]

    for i in range(len(arr)):
        size = len(str(arr[i]))
        bucket[size-1].append(arr[i])

    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])

    result = []
    for each in bucket:
        result += each

    print(result)


bucketSort()
