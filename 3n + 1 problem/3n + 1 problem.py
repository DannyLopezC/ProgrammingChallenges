#given range
i = int(input())
j = int(input())
#C is the current number that will be evaluating
currentNumber = i
#list of cycle lengths
counters = []

while currentNumber <= j:
    n = currentNumber
    counter = 1
    while not n == 1:
        counter += 1

        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int((n*3) + 1)
    currentNumber += 1

    counters.append(counter)

counters.sort(reverse=True)

if j < i:
    print("Error", j, "is less than", i)
else:
    maxCounter = counters[0]
    print(str(i) + " ", end='')
    print(str(j) + " ", end='')
    print(str(maxCounter) + " ", end='')

