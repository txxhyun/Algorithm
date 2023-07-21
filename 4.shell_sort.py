def shell_sort(a): # 쉘 정렬
    n = len(a)
    gap = n//2
    while gap >= 1:
        if (gap%2) == 0 : gap += 1 #gap이 짝수면 +1 을 해서 홀수로 만들어줌
        for i in range(gap,n):
            j=i
            while j >= gap and a[j] < a[j-gap]: #j-gap 을 통해 앞 배열 체크
                a[j],a[j-gap] = a[j-gap], a[j]
                j -= gap 
        print('    Gap=',gap,a)
        gap = gap//2

data = [5,3,8,4,9,1,6,2,7]
print('Original :',data)
shell_sort(data)
print('Shell    :', data)