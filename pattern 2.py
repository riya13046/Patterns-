def pattern(n):
    for i in range(n):
            if i%2==0:
                print((n-i)*'o',end=" ")
            else:
                print((n-(i-1))*'*',end=" ")
            print()
a=int(input())
pattern(a)
