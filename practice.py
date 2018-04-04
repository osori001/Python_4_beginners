# 1. Character input
"""
name = input("What is your name: ")
print ("Your name is "+name)
"""

# 2. Odd or Even

num = input("Give me a number: ")
if num.isdigit() == True:
    if int(num) % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"
    print ("Your number is "+oddeven)
else:
    print ("aint a number")

# 3. List Less Than Ten
