import random
import time
#implementation of binary search algo

#Will prove that binary search is faster than naive search

#Naive search: scan entire list and ask if it's equal to the target
#if yes, rturn the index
#if no, then return -1

def naive_search(l, target):
    #example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1



def binary_search(l, target, low = None, high = None):

        if low is None:
            low =0
        if high is None:
            high = len(l)-1

        #returns -1 to indicate the midpoint is not in the list
        if high < low:
            return -1

        # midpoint is the length of the list divided by two
        midpoint = (low+high) // 2

        #if the midpoint is equal to the target, it returns the index
        if l[midpoint] == target:
            return midpoint
        
        #use recursion on the left side of the list where lower values are
        elif target < l[midpoint]:
            return binary_search(l, target, low, midpoint-1)
        else:
            #use recursion on the right side of the list where higher values are
            #
            return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

    #initalizing a random sorted list
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    
    #make the sorted list into a list and then sort
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    #naive_search is iterated 10000 times for each element on the list and timed
    for target in sorted_list:
        naive_search(sorted_list, target)
    
    end = time.time()
    print ("Naive search time: ", (end - start)/length)


    
    start = time.time()
    #naive_search is iterated 10000 times for each element on the list and timed
    for target in sorted_list:
        binary_search(sorted_list, target)
    
    end = time.time()
    print ("Binary search time: ", (end - start)/length)


