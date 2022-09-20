# Write a function that flattens a list.

inPut = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
outPut = []

def flattenList(l):
    for i in l:
        if isinstance(i,list):
            flattenList(i)
        else:
            outPut.append(i)
    return outPut
    
flattenList(inPut)
