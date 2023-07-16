def insert(self, intervals, newInterval):
    # insert new interval into intervals
    intervals.append(newInterval)
    if len(intervals) <= 1:
        return [intervals[0]]
    list = []
    # print(intervals)
    intervals.sort()
    prevStart, prevEnd = intervals[0]

    # print(intervals)
    intervals.remove([prevStart, prevEnd])
    for start, end in intervals:
        if prevEnd >= start and prevEnd <= end:
            prevEnd = end
            prevStart = min(start, prevStart)
        elif prevEnd >= start and prevEnd > end:
            continue
        else:
            list.append([prevStart, prevEnd])
            prevStart, prevEnd = start, end

    list.append([prevStart, prevEnd])
    return list
