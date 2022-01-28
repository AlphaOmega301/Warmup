#for loop
"""
digit = int(input())
for num in range(1,10):
    print (digit, "x", num, "=", digit*num)

for num in range(1,31) :
    if num % 3 == 0 :
        print(num)
"""
#while loop
"""
password = "7621"
data = str()

while data != password :
    data = input()
    if data == password :
        print ("Right Password")
        break
    else:
        print ("Wrong Password")
"""
#List

num_list = [0, -11, 31, 22, -11, 33, -44, -55]
num_list2 = list()

for index, num in enumerate(num_list):
    if num >= 0 :
        num_list2.append(num)

print(num_list2)
