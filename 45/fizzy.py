


def fizzbuzz(i):
    """
    Returns numbers from 1 to 100.
    If the number is divisible by 3 returns fizz.
    If the number is divisible by 5 returns buzz.
    If the number is divisible by 3 and 5 then returns fizzbuzz.
    """
    if (i%3 == 0) and (i%5 == 0):
    	return 'fizzbuzz'
    elif (i%5 == 0):
    	return 'buzz'
    elif (i%3 == 0):
    	return 'fizz'
    else:
    	return i
    	 

for i in range(1,101):
    number = fizzbuzz(i)
