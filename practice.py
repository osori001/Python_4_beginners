# 1. Character input
"""
name = input("What is your name: ")
print ("Your name is "+name)
"""

# 2. Odd or Even
"""
num = input("Give me a number: ")
if num.isdigit() == True:
    if int(num) % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"
    print ("Your number is "+oddeven)
else:
    print ("aint a number")
"""
# 3. List Less Than Ten
"""
schindlers = []
#####asks user for input to create a list.
mten = 0
while mten < 10:
    num = input("Give me your number for index %d : " % (mten))
    if num.isdigit() == True:
        schindlers.append(int(num))
        mten += 1
    else:
        print ("invalid input.")

ltt = []
#####filters initial inputs for less than ten.
for s in range(0,10): #range(a,b) formatted from a to b-1
    if schindlers[s] < 10:
        ltt.append(schindlers[s])

print (ltt)
"""
#4. Divisors

