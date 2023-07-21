def binary_search(A,key,low,high): #정렬된 배열의 탐색에 적함, 재귀버전임
    if (low <= high) :
        middle = (low+high)//2
        if key == A[middle]:
            return middle
        elif (key < A[middle]):
            return binary_search(A,key,low,middle-1)
        else :
            return binary_search(A,key,middle+1,high)
    return None

key = int(input())
a = list(map(int, input().split(' ')))
N = len(a)
print(f' {binary_search(a,key,0,N-1)}')