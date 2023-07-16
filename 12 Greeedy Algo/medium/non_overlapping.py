def eraseOverlapIntervals(intervals):
    if len(intervals) <= 1:
        return 0

    count = 0
    intervals.sort()
    prevStart, prevEnd = intervals[0]
    intervals.remove([prevStart, prevEnd])

    for start, end in intervals:
        if prevEnd >= start and prevEnd <= end:
            prevEnd = end
            prevStart = min(start, prevStart)
            count += 1
        elif prevEnd >= start and prevEnd > end:
            continue
        else:
            # list.append([prevStart, prevEnd])
            prevStart, prevEnd = start, end

    return count

 
print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
