def getSingleElement(a):
    
    a.sort()

    for i in range(1,len(a)):
            if a[i]!=a[i-1]:
                  return
    
    pass