A = [1,2,9,3,4,6,11,15]
#A = [-1,-2,-5]

def solution(A):
    B = [i+1 for i in A if i+1 not in A]
    for i in range(0,len(B)):
        if B[i] < 0:
            B.pop(i)
    for i in range(0,len(B)):
        if B[0] > 0 :
            if len(B) ==1:
                return (B[0])
            if B[0] > B[-1]:
                B.pop(0)
            else:
                B.pop(-1)

    return (1)

print (solution(A))

