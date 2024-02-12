temperature = 32

if temperature > 37:
    print("It's hot")
else:
    print("It's cold")

# A program that prints the > number among 3 numbers
q = 12
w = 23
e = 63
if q > w and q > e:
    print(q, "is the largest number")
elif w > q and w > e:
    print(w, "is the largest number")
else:
    print(e, "is the largest number")

# A program that checks whether a number is even or odd
number = 56
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")



n = 0
if n>1:
 for i in range(2,n//2):
     if(n%i)==0:
        print(n,"is not a prime number")
     break
 else:
     print(n,"is a prime number")
else:
    print(n,"is neither prime nor composite")

