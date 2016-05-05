#Victor
#Junjie Lin


def factorial (n: int) -> int:
    '''compute n! (n factorial) '''
    if n <=0:
        return 1
    else:
        return n * factorial(n - 1)
assert(factorial(0) == 1)
assert(factorial(5) == 120)

print("10! is", factorial(10))
print("100! is", factorial(100))

