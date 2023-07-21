def binary_search(A,key,low,high): #이진탐색 재귀
    if (low <= high) :
        middle = (low+high) // 2
        if key == A[middle]:
            return middle
        elif key < A[middle] :
            return binary_search(A,key,low, middle-1)
        elif key > A[middle] :
            return binary_search(A,key,middle+1, high)
    return high #바뀐 부분

key = int(input())
a = list(map(int, input().split(' ')))
N = len(a)
print(f' {binary_search(a,key,0,N-1)}')

k= int(input())
l = list(map(int,input().split()))