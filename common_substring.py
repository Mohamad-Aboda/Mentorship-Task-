# problem two
# O(len(s1) * len(s2))
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