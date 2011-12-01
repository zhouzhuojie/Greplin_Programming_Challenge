def isPrime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def Fibonacci():
    """Fibonacci Generator """
    a,b = 0, 1
    while True:
        yield a
        a, b = b, a+b

def minFibPrimeOver(n):
    f = Fibonacci()
    while True:
        a = f.next()
        if a <= n:
            continue
        if isPrime(a):
            return a

if __name__=='__main__':
    a = minFibPrimeOver(227000)
    l = [i for i in xrange(2, int(a**0.5) + 1) if (a+1)%i==0 and isPrime(i)]
    print sum(l)
