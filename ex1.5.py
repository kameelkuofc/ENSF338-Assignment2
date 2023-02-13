import timeit
from matplotlib import pyplot as plt
## 
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

## optimized code
def func_opt(n, fib_no = {}):
    if n == 0 or n == 1:
        return n
    if n in fib_no:
        return fib_no[n]
    fib_no[n] =  func_opt(n-1, fib_no) + func_opt(n-2, fib_no)  
    return fib_no[n]  



fib_time = []
opt_fib_time = []
i = 0 
for i in range(0, 36):
        fib_time.append(timeit.timeit(lambda:func(i)))
        opt_fib_time.append(timeit.timeit(lambda: func_opt(i)))

plt.hist(fib_time, label ='Original Function')
plt.hist(fib_time, label ='Optimized Function')
plt.legend(loc = 'upper right')
plt.show()





       


