k= int(input())
l = list(map(int,input().split()))

def binary_search(A,key,low,high): #이진 탐색 비재귀
    while (low <= high):
        middle = (low+high)//2
        if key == A[middle]:
            return middle
        elif (key<A[middle]):
            high = middle-1
        else:
            low = middle+1
    return high+1

length = len(l)
l.sort()
high = length -1

result = binary_search(l,k,0,high)
print('',result)