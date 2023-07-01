def atMostKDistinct(nums, k):
        hashmap = {}
        subarrays = 0
        start, end = 0, 0
        while end < len(nums):
            if nums[end] in hashmap:
                hashmap[nums[end]] += 1
            else:
                hashmap[nums[end]] = 1
            while len(hashmap) > k:
                hashmap[nums[start]] -= 1
                if hashmap[nums[start]] == 0:
                    del hashmap[nums[start]]
                start += 1
            subarrays += end-start+1
            end += 1
        return subarrays

print(atMostKDistinct([1,2,1,2,3], 2)-atMostKDistinct([1,2,1,2,3], 2-1))