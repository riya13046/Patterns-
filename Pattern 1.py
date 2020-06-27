def fun(n):
    for i in range(n):
            if i%2==0:
                print((n-i)*'*',end=" ")
            else:
                print((n-(i-1))*'*',end=" ")
            print()
n=int(input())
fun(n)
