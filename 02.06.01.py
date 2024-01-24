n = 3

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

mass = []
for i in range(factorial(n), 0, -1):
    i = factorial(i)
    mass.append(i)
print(mass)
  