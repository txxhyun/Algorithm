def insertion_sort(a): #삽입 정렬
    for i in range(1,len(a)): # 1부터 len(a)-1까지 반복, 0번째 원소는 이미 정렬되었다고 가정하고 시작, 어차피 안쪽 반복문에서 처리해줌
        for j in range(i,0,-1): # i부터 1까지 감소하면서 숫자 비교
            if a[j-1] > a[j]: # j-1이 0까지 커버해주기 때문에 i부터 1까지 감소하면수 for 문 돌아감
                a[j], a[j-1] = a[j-1], a[j]

a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전 :\t', end = '')
print(a)
insertion_sort(a)
print('정렬 후 :\t', end = '')
print(a)