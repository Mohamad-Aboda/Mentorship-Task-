# problem one 
# O(n * n)

# def absolute_defference():
#     n = int(input())
#     arr = list(map(int, input().split()))

#     mn = 1000000007
#     for i in range(n):
#         for j in range(i+1,n):
#             if abs(arr[i]-arr[j]) < mn:
#                 mn = abs(arr[i] - arr[j])

#     return mn




# O(n*log(n))
def absolute_defference():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort() 

    mn = abs(arr[1] - arr[0])
    for i in range(2, n):
        if abs(arr[i] - arr[i - 1]) < mn:
            mn = abs(arr[i] - arr[i - 1])
    return mn


res = absolute_defference()
print(res)


