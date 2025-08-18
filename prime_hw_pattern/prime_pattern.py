# prime number 

def prime(n):
    r=(n//2)+1
    count=0
    for i in range(2,r):
        if n % i ==0:
            count+=1
    if count==0:
        print(f"{n} is a prime number")

for j in range(1,101):
    prime(j)