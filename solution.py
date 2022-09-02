import math as np
def solution(n):
    l=[]
    j=0
    max_while=10000000
    while n>0:
        x=range(n+1)[::-1]
        first=list( map(np.sqrt,x))
        second=[-xx for xx in map( int, map(np.sqrt,x))]
        i=[sum(value) for value in zip(first, second)].index(0)        
        l.append(x[i])        
        n=n-x[i]
        j+=1
        if j>max_while:
            break
    return l
if __name__=='__main__':
    print('tests..')
    assert solution(12)==[9, 1, 1, 1]
    assert solution(15324)==[15129,169,25,1]    
