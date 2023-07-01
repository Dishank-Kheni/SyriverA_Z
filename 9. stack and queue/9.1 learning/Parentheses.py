from collections import deque


def isValid(s):
    deQueue = deque()

    para = {'(':")",'[':"]","{":"}"}
    
    for each in s:
        try:
            if each in para.keys():
            # if para.get(para):
                deQueue.append(each)
            else:
                if para[deQueue.pop()] != each:
                    return False
        except:
            return False

    if len(deQueue)>0:
        return False
    else:
        return True
    # print(deQueue)


print(isValid(")[()]"))
    