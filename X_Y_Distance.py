#A = [1,2,9,3,4,6,11,15]
A = [-1,-2,-5]



def solution(A,B,C,D):
    test = []
    test_max = []
    test_min = []
    test.append(A)
    test.append(B)
    test.append(C)
    test.append(D)
    test_max.append(max(test))
    test_min.append(min(test))
    test.remove(max(test))
    test.remove(min(test))
    test_max.append(max(test))
    test_min.append(min(test))
    x = (test_max[0] - test_min[0])
    y = (test_max[1] - test_min[1])
    print (x)
    print (y)
    
    
    return (x*x + y*y)


print (solution(1,2,3,4))



#print (solution(-1,2,3,-4))

#print (solution(-1,-1,-3,-4))



