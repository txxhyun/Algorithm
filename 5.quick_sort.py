def quick_sort(A,left,right): #재귀 함수임 분할 정복법 사용.
    if left < right :
        q = partition(A,left,right)
        quick_sort(A,left,q-1)
        quick_sort(A,q+1,right)

def partition(A,left,right): #분할하는 함수
    low = left + 1
    high = right
    pivot = A[left] #핵심인 피벗
    while (low <= high): # low가 high보다 작을면 계속 반복
        while low <= right and A[low] < pivot : low += 1 # low가 right보다 작고, low값이 피벗보다 작으면 low 값 +1 즉, low값 이동
        while high >= left and A[high] > pivot : high -=1 # high가 left보다 크거나 같고, high값이 피벗보다 크면 high 값 -1 즉, high값 이동

        if low < high : # 위의 while문이 끝나고, 즉 교환조건임 low의 값이 피벗보다 크고, high값이 피벗보다 작을때,
            A[low],A[high] = A[high], A[low] #low위치와 high위치의 값들을 교환
    
    A[left],A[high] = A[high],A[left] # 
    return high

A = [5,3,8,4,9,1,6,2,7]
quick_sort(A,0,len(A)-1)
print(A)