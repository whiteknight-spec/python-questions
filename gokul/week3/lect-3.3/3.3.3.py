# find the factorial of a number using while loop, take number n as input
n = int(input())
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print(fact)
