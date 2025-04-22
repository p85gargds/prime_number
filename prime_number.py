#taking input from user
lower = int(input("Enter a number:"))
upper = int(input("Enter another number:"))
print("Prime numbers between",lower,"and",upper)
#iterate loop from lower limit to upper limit
for num in range(lower , upper + 1):
#using loop to identify prime number
    if num > 1:
        for j in range(2,num):
            if ( num % j) == 0:
                break
            
        else:
            print(num)
    