
# while loop examples : 
#  while loop will give an limit to the code
#  in below example the age is 10 , the while loop is <18 that means the while  loop will run until 18 years.
#  is the age is more than 18 then while loop will not print you are no eligible.
age =10
while age <18:
    print("you are not eligible")
    print("line5",age)
    age =age+1
    print("line6",age)



#  in the example starting number is given as 1 and the while loop will run until less than 10 
number=1
while number <10:
    print(number)
    number+=1

#  print numbers with there sqauare while n < 11
n=1
while n <11:
    print(n,"",n**2)
    n=n+1
    
    #  print numbers from 105 until the number is small than 7 with commmas
n=105
while n>7:
    print(n-7,end=",")
    n=n-7

#  print number untill n <300 with addition of n+10 in each element
n=0
while n<300:
    print(n+10,end=",")
    n=n+10

#  while loop from back to start
n=11
while n >1:
    print(n-1)
    n=n-1

#  printing number + number untill number is less than 11.
n=1
while n<11:
    print(n+n,end=",")
    n=n+n
    
