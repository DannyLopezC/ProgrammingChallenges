i = 900
j = 1000
c = i
counters = []
while c <= j:
    n = c
    counter = 1
    while not n == 1:
        counter += 1
        """ print(str(n) + " ", end='') """
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int((n*3) + 1)
    c += 1
    """ print(n) """
    counters.append(counter)
    """ print(counter) """

counters.sort(reverse=True)
maxCounter = counters[0]

print(str(i) + " ", end='')
print(str(j) + " ", end='')
print(str(maxCounter) + " ", end='')
