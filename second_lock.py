def second_lock(arr):
    door_locked = True
    counter_store = 0
    pointer = 1
    arr_sementara = []
    arr_res = []
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == pointer:
            arr_res.append(arr[i])
            arr.remove(arr[i])
            
            counter_store = counter_store
            pointer += 1
            # print(arr) #debug
            # print(arr_res) #debug

        else:
            index_pointer = arr.index(pointer)
            if arr[index_pointer-1] > pointer and arr[i] < arr[i-1]:
                door_locked = False
                counter_store = -1
                break

            else:
                counter_store += 1
                 

    
    return door_locked, counter_store




    
print(second_lock([4, 3, 2, 1])) #T 0
print(second_lock([1, 2, 3, 4, 5])) #T 4
print(second_lock([6, 1, 4, 5, 2, 3])) #F -1
print(second_lock([3, 4, 5, 2, 1])) #T 2

print(second_lock([4, 5, 3, 6, 2, 1])) #T 2

print(second_lock([18, 16, 17, 15, 14, 11, 12,13, 10, 9, 7, 8, 6, 4, 5, 2, 3, 1])) #T 2
