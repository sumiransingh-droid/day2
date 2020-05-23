def isPrime(N):
   a = 2
   k = N // 2
   while k >= a:
       if N % a == 0:
           return False 
       a += 1
       k = N // a
    return True
 
    
def ispalindrome(n):
   N = str(n)
   L = len(n)
   for i in range(L//2):
       if N[i] != N[ L - 1 - i ]:
           return False 
       return True 
       
  
def isodd(n):
if n % 2 == 0:
   return False 
return True
         
         
def isArmstrong(num): 
   sum == 0
   temp == num 
   while temp > 0:
       digit = temp % 10
       sum+= digit ** 3
       temp // = 10
    if num == sum:
      return True 
    return False 
    
    
def check():
    number=int(input("enter the number "))
    if (isprime(number)):
        print(number,"is a prime number")
    if (isodd(number)):
        print(number,"is odd number ")
    else:
        print(number,"is even number ")
    if (isPalindrome(number)):
        print(number,"is palindrome number")
    if (isArmstrong(number)):
        print(number,"is Armstrong number ")
check()
    	
