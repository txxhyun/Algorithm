def merge_sort(A,left,right) : #병합정렬
    if left<right :
        mid = (left+right) // 2
        merge_sort(A,left,mid)
        merge_sort(A,mid+1,right)
        merge(A,left,mid,right)

def merge(A,left,mid,right):
    global sorted
    k = left
    i = left
    j = mid + 1
    while i<=mid and j<=right:
        if A[i] <= A[j] :
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid :
        sorted[k:k+right-j+1] = A[j:right+1]
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]
    A[left:right+1] = sorted[left:right+1]

A = [27,10,12,20,25,13,15,22]
merge_sort(A,1,len(A)-1)
print(A)
