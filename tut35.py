# Recursions: Recursive Vs Iterative Approach

def factorial(n):
    """
    :param n:
    :return:
    """

    # iterative approach
    # fac = 1
    # for i in range(n):
    #     fac = fac * (i+1)
    # return fac

    # Recursive approach
    if n == 1:
        return 1
    return n * factorial(n-1)

# a = int(input("Enter the number : "))
# print(factorial(a))

def fib(n):
    if n == 0 or n == 1:
        return n

    # t[0] =0
    return fib(n-1) + fib(n-2)

n = int(input("Enter n : "))
for i in range(n):
    print(fib(i), end=" ")