def func(n, fib_no = {}):
    if n == 0 or n == 1:
        return n
    if n in fib_no:
        return fib_no[n]
    fib_no[n] =  func(n-1, fib_no) + func(n-2, fib_no)  
    return fib_no[n]  

