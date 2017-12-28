
A = [6,1,4,6,3,2,7]
B = [6,1,4,6,]
K = 3
L = 2

def solution(movies, K, L):
    K_movie = []
    K_max = []
    L_movie = []
    L_max = []
    K_value = 0
    L_value = 0
    if K+L > len(movies):
        return (-1)


    for i in range (0,len(movies)):

        if len(movies) > movies.index(max(movies)) + L:
            
            if movies.index(max(movies)) < K:
                K_movie = movies[0:K]
                L_movie = movies[K:]
            else:
                print(2)
                K_movie = movies[0:movies.index(max(movies))]
                L_movie = movies[movies.index(max(movies)):]

        else:
            L_max.append(max(movies))
            movies[movies.index(max(movies))] = 0

    for i in range(0,K):
        K_max.append(max(K_movie))
        K_movie.remove(max(K_movie))

    for i in range(0,L-len(L_max)):
        L_max.append(max(L_movie))
        L_movie.remove(max(L_movie))


    for i in K_max:
        K_value += i

    for i in L_max:
        L_value +=i

    return (K_value + L_value)

    



print (solution(A, K, L))


