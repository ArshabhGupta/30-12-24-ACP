a = int(input("Enter a number: "))
count1 = 0
count0 = 0
binary = bin(a)
binary = binary[2:]
print(binary)
for i in binary:
    if i == '1':
        count1 += 1
    else:
        count0 += 1
print("The longest sequence of 1s is:", count1)
print("The longest sequence of 0s is:", count0)