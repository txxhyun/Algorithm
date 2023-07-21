def printStep(arr,val):
    print("Step %2d ="%val, end='')
    print(arr)

def bubble_sort(A): # 버블정렬
    n = len(A)
    for i in range(n-1,0,-1): #전체 스캔 횟수 & 오른쪽에서 왼쪽으로 감소하면서 반복
        is_sorted = True #정렬이 되었는가?
        for j in range(i): # 스캔 한번에서의 전체 탐색 & 오른쪽 끝으로 가장 큰수를 보냄 & 오른쪽에서 부터 큰 수로 정렬되어있음
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                is_sorted = False #정렬이 아직 다 안됐음을 표현
        if is_sorted : #정렬이 되었으면 빠져나가고 프린트 스텝 i 
            break
        printStep(A,n-i)

A = [5,3,8,4,9,1]
print("Origianl:", end='')
print(A)
bubble_sort(A)
print("Bubble\t", A)