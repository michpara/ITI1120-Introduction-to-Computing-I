def min_or_max_index(lst, flag):
    max_val = lst[0]
    min_val = lst[0]
    if flag:
        for i in lst:
            if i < min_val:
                min_val = i
        return (min_val, lst.index(min_val))
    else:
        for i in lst:
            if i > max_val:
                max_val = i
        return (max_val, lst.index(max_val))
                
        

