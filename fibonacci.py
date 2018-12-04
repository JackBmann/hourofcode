from sys import stdin

fibonacciNumbers = {0: 0, 1: 1}


def fibonacci(i):
    if i not in fibonacciNumbers:
        fibonacciNumbers[i] = fibonacci(i-1) + fibonacciNumbers[i-2]
    return fibonacciNumbers[i]


targetNum = int(stdin.readline().strip())
print(fibonacci(targetNum))

fibonacciSequence = ""
for num in fibonacciNumbers:
    fibonacciSequence += str(fibonacciNumbers[num]) + ", "
fibonacciSequence = fibonacciSequence[:-2]

with open("fibonacci.txt", 'w') as f:
    f.write(fibonacciSequence)
