
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__=="__main__":
    print("Valor de factorial de 5: ")
    print(factorial(5))
    print("Valor de fibonacci de 8: ")
    print(fibonacci(8))