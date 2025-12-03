#import math

banks = []
while True:
    bank = input()
    if not bank:
        break
    banks.append(bank)
#print(banks)

# total = 0
# while banks:
#     currentBank: str = banks.pop()
#     firstDigit = 0
#     for i in range(len(currentBank)-1):
#         if int(currentBank[i]) > firstDigit:
#             firstDigit = int(currentBank[i])
#     #print(firstDigit)
#     secondDigit = 0
#     for j in currentBank[currentBank.index(str(firstDigit))+1:]:
#         if int(j) > secondDigit:
#             secondDigit = int(j)
#     #print(secondDigit)
#     #print((10*firstDigit) + secondDigit)
#     #print('-------------------')
#     total += (10*firstDigit) + secondDigit

# print(total)

total = 0
while banks:
    #subtotal = 0
    currentBank: str = banks.pop()
    startIndex = 0
    for i in range(11, -1, -1):
        compareDigit = 0
        #print(currentBank[startIndex:len(currentBank)-i])
        for j in range(startIndex, len(currentBank)-i):
            if int(currentBank[j]) > compareDigit:
                compareDigit = int(currentBank[j])
                startIndex = j+1
        #subtotal += compareDigit*pow(10,i)
        total += compareDigit*pow(10,i)
    #print(subtotal)

print(total)