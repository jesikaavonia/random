def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))

def first_lock(arr):
    mp = dict()
    # Traverse through array elements
    # and count frequencies
    res = []
    n = len(arr)

    if n == 1:
        res.append(arr[0])
        return res


    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

           
    # Traverse through map and print
    num = 0
    for x in mp:
        if mp[x]!=1 :
            res.append(x)
            num += 1
            # print(x)
    return res



print(quicksort(first_lock(["topaz"]))) 
print(quicksort(first_lock(['ruby','ruby','diamond','amethyst']))) 
print(quicksort(first_lock(['ruby','ruby','diamond','diamond','amethyst']))) 
