from time import time

def mySort(alist): #only works with lists of integers
    if len(alist) < 2:
        return alist

    floatDetected = False
    biggest = alist[0]
    smallest = alist[0]
    for num in alist:
        if num > biggest:
            biggest = num
        elif num < smallest:
            smallest = num
        else:
            pass
        if num % 1 != 0 and floatDetected == False:
            floatDetected = True
            print("Float detected. Can not sort.")
            return alist
            break

    if biggest == smallest: #alist only contains (repeats of) one number
        return alist
            
    range_of_alist = biggest - smallest +1

    #prevent crashing from creating a large tempList[] and/or increases speed by
        #removing large gaps that would be created in tempList[]
    if range_of_alist > 150000000 or range_of_alist // len(alist) > 500:
        smallHalf = []
        bigHalf = []
        midPoint = (biggest + smallest) / 2
        for num in alist:
            if num < midPoint:
                smallHalf.append(num)
            else:
                bigHalf.append(num)
        return mySort(smallHalf) + mySort(bigHalf)
    
    else:

        #if range_of_alist is over two-hundred million, the program returns a
            #memory error and quits. This is prevented by the above 'if' statement.
        tempList = [None] * range_of_alist        
        for num in alist:
            if tempList[num-smallest] == None:
                tempList[num-smallest] = [num]
            else:
                #the number is a duplicate
                tempList[num-smallest].append(num)

        #put numbers together in a sorted list
        transitionList = []
        position = 0
        for sublist in tempList:
            if sublist != None:
                for item in sublist:
                    alist[position] = item
                    position += 1
            else:
                pass

        return alist

def testTime():
    for i in range(10000, 100001, 10000):
        alist = []
        for j in range(i):
            alist.append(100000000 // i * j)
            #alist.append(randint(0, i)) #allows for possible duplicates
        alist = alist[:len(alist)//2] + alist[:len(alist)//2] #forces duplicates
        #alist.append(99000000) #forces a large range by using an outlier (probably an outlier)
        start = time()
        for j in range(10):
            sortedList = mySort(alist)
        print((time() - start)/10)
        start = time()
        for j in range(10):
            alist.sort()
        print((time()-start)/10)

def testSorting():
    a = [1,2,3,4,4,3,23,1,-543,-56789,0,0]
    b = mySort(a)
    print(b)
