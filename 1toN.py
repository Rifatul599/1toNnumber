def fun(N):
    if N == 0 :
        return
    else:
        fun(N-1)
        print(N)

fun(100)