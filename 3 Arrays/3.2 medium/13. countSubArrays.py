from collections import defaultdict


def findAllSubarraysWithGivenSum(a, k):
    count = 0

    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum > k:
                break
            elif sum == k:
                count += 1
                break

    return count


print(findAllSubarraysWithGivenSum([3, 1, 2, 4], 6))
print(findAllSubarraysWithGivenSum([1, 2, 3], 3))

# inspiring


def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr)  # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1  # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt
