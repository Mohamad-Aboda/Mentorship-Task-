# problem one 
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


#problem two 
def two_strings(s1, s2):
    ok = False 
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s2[j] in s1[i]:
                ok = True 
                break 
    
    if ok:return True 
    else:return False 
    

res = two_strings('cat', 'art')
print(res)