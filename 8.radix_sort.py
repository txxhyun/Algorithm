from queue import Queue # 기수 정렬
def radix_sort(A):
    queues = [] #큐의 리스트
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1 #1의 자리부터 시작
    for d in range(DIGITS): #모든 자리에 대해
        for i in range(n): #자릿수에 따라 큐에 삽입
            queues[(A[i]//factor) % 10].put(A[i]) # 숫자를 삽입
        i = 0
        for b in range(BUCKETS) :
            while not queues[b].empty():
                A[i] = queues[b].get()
                i += 1
        factor *= 10
        print("step",d+1,A)

import random
BUCKETS = 10 # 10진수를 의미함
DIGITS = 4 # 4자리 수를 의미함
data = []
for i in range(10): #만들려는 숫자의 갯수를 정함
    data.append(random.randint(1,9999)) #4자리 수가 나와야하므로 1~9999까지 무작위 추출 
radix_sort(data)
print("Radix: ", data)
