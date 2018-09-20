def dirReduc(arr):
    new_list = arr.copy()
    while has_touching(new_list):
        for i, _ in enumerate(new_list):
            if i == len(new_list)-1:break
            if compare_two(new_list[i],new_list[i+1]):
                del new_list[i+1]
                del new_list[i]
    return new_list
    
def compare_two(a, b):
    n, s, w, e = 'NORTH','SOUTH','WEST','EAST'
    if [a,b] in [[n,s],[s,n],[w,e],[e,w]]:
        return True
    return False
    
def has_touching(dirs):
    for i in range(0,len(dirs)-1):
        if compare_two(dirs[i],dirs[i+1]):
            return True
    return False
