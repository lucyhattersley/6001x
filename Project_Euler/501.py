def findDivs(number):
    divisors = []
    i = 1
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

#result = 0
#
#for i in range(1, (10**6)+1):
#    if findDivs(i) == 8:
#        result += 1
#
#print result

def findDivsBi(number):
    divisors = []
    low = 1
    hi = number
    guess = ((low + hi) // 2)
    if number % guess == 0:
        divisors.append(guess)
        # find lows
        low = low
        hi = guess
        guess = ((low + hi) // 2)
        return findDivsBi(guess)
    
        # find his
        low = guess
        high = high
        guess = ((low + hi) // 2)
        return findDivsBi(guess)
    else:
        return
    return divisors