def sjf(arrivalTime, burstTime):

    # print(sorted(arrivalTime, (lambda x: x[1])))

    dict = [[k, v] for k, v in zip(arrivalTime, burstTime)]
    completeTime = []
    waitingTime = []
    turnAroundTime = []
    dict.sort()
    waiting = 0
    complete = 0
    for each in dict:
        complete += each[1]
        completeTime.append(complete)
        waitingTime.append(waiting)
        waiting += each[1]
    print(dict)
    print(completeTime)
    print(waitingTime)
    turnAroundTime = [x - y for x, y in zip(completeTime, arrivalTime)]
    print(turnAroundTime)


# sjf([0, 0, 0, 0, 2, 4, 5], [7, 4, 2, 3, 4, 1, 4])
sjf([0, 0, 0], [4, 2, 3])
