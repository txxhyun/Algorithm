def selection_sort(a): #선택 정렬
    for i in range(0,len(a)-1): #0번 인덱스부터 끝 인덱스까지 전부 반복
        minimum = i
        for j in range(i,len(a)): # 정렬이 안된부분부터 끝까지
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i] # 현재 원소와 정렬 안된 부분에서의 최솟값 교환

a = [54,88,77,26,93,17,49,10,17,11,31,22,44,17,20]
print('정렬 전:\t', end='')
print(a)
selection_sort(a)
print('정렬 후:\t', end='')
print(a)

# def insertion_sort(a): #삽입 정렬
#     for i in range(1,len(a)): # i부터 len(a)-1까지 반복, 0번째 원소는 이미 정렬되었다고 가정하고 시작 어차피 안쪽 반복문에서 처리해줌
#         for j in range(i,0,-1): # i부터 1까지 감소하면서 숫자 비교
#             if a[j-1] > a[j]:
#                 a[j], a[j-1] = a[j-1], a[j]

# a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
# print('정렬 전 :\t', end = '')
# print(a)
# insertion_sort(a)
# print('정렬 후 :\t', end = '')
# print(a)


# def bubble_sort(A): # 버블정렬
#     n = len(A)
#     for i in range(n-1,0,-1): #전체 스캔 횟수
#         for j in range(i): # 스캔 한번에서의 전체 탐색 
#             if A[j]>A[j+1]:
#                 A[j], A[j+1] = A[j+1], A[j]

# A = [5,3,8,4,9,1,6,2,7]
# bubble_sort(A)
# print(A)

# def shell_sort(a): # 쉘 정렬
#     n = len(a)
#     gap = n//2
#     while gap >= 1:
#         if (gap%2) == 0 : gap += 1 #gap이 짝수면 +1 을 해서 홀수로 만들어줌
#         for i in range(gap,n):
#             j=i
#             while j >= gap and a[j] < a[j-gap]:
#                 a[j],a[j-gap] = a[j-gap], a[j]
#                 j -= gap
#         print('    Gap=',gap,a)
#         gap = gap//2

# data = [5,3,8,4,9,1,6,2,7]
# print('Original :',data)
# shell_sort(data)
# print('Shell    :', data)

# def merge_sort(A,left,right) : #병합정렬
#     if left<right :
#         mid = (left+right) // 2
#         merge_sort(A,left,mid)
#         merge_sort(A,mid+1,right)
#         merge(A,left,mid,right)

# def merge(A,left,mid,right):
#     global sorted
#     k = left
#     i = left
#     j = mid + 1
#     while i<=mid and j<=right:
#         if A[i] <= A[j] :
#             sorted[k] = A[i]
#             i, k = i+1, k+1
#         else:
#             sorted[k] = A[j]
#             j, k = j+1, k+1

#     if i > mid :
#         sorted[k:k+right-j+1] = A[j:right+1]
#     else:
#         sorted[k:k+mid-i+1] = A[i:mid+1]
#     A[left:right+1] = sorted[left:right+1]

# A = [27,10,12,20,25,13,15,22]
# merge_sort(A,1,len(A)-1)
# print(A)

# from queue import Queue # 기수 정렬
# def radix_sort(A):
#     queues = [] #큐의 리스트
#     for i in range(BUCKETS):
#         queues.append(Queue())

#     n = len(A)
#     factor = 1 #1의 자리부터 시작
#     for d in range(DIGITS): #모든 자리에 대해
#         for i in range(n): #자릿수에 따라 큐에 삽입
#             queues[(A[i]//factor) % 10].put(A[i]) # 숫자를 삽입
#         i = 0
#         for b in range(BUCKETS) :
#             while not queues[b].empty():
#                 A[i] = queues[b].get()
#                 i += 1
#         factor *= 10
#         print("step",d+1,A)

# import random
# BUCKETS = 10 # 10진수를 의미함
# DIGITS = 4 # 4자리 수를 의미함
# data = []
# for i in range(10): #만들려는 숫자의 갯수를 정함
#     data.append(random.randint(1,9999)) #4자리 수가 나와야하므로 1~9999까지 무작위 추출 
# radix_sort(data)
# print("Radix: ", data)



