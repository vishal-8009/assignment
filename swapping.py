# to swap two numbers

num1= int(input("Enter a number"))
num2 = int(input("Enter another number:"))

print(f"before swapping: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1
print(f"after swapping: num1 = {num1}, num2 = {num2}")