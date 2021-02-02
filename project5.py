def isDivisibleBy(num, divisor):
	''' function returns True if num is divisible by divisor '''
	if num % divisor == 0:
		return True
	else:
		return False

def isOdd(num):
	''' function returns True if num is odd '''
	if isDivisibleBy(num,2):
		return False
	else:
		return True

def isPrime(number):
    factors = 0
    for i in range(1,number+1):
        if number %i ==0:
            factors +=1
    if factors == 2:
        return True
    else:
        return False
            

def hasFourFactors(number):
   factors = 0
   for i in range(1,number+1):
        if number %i ==0:
            factors +=1
   if factors == 4:
        return True
   else:
        return False

# main body of code
N = 22022 # my 5 digit unique number

# compute A
A = 0 
for num in range(1,N+1):
    if isDivisibleBy(num,7):
        A += 1
        
# compute B
B = 0 
for num in range(1,N+1):
    if isPrime(num):
        B += 1

# compute C
C = 0 
for num in range(1,N+1):
    if hasFourFactors(num):
        C += 1
        
result = A + B + C
print(result)
