def fibonacci(x):
    f0,f1=0,1
    result=0
    for f in range(x):
        result=f0+f1
        f0=f1
        f1=result
    return(result)


for i in range(10):
    print(i, fibonacci(i))
