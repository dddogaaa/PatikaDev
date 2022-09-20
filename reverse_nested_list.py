ex_list = [[1, 2], [3, 4], [5, 6, 7]]

def list_reverse(l):
    for i in l:
        if isinstance(i,list):
            i.reverse()
        l.reverse()
    return l

list_reverse(ex_list)
    
