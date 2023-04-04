from operator import mul
print('Input the amount you want to calcluate VAT on')
x = int(input())

result = x * 20 / 100
total = x + result

print('The VAT amount is')
print(result)

print('The total amount including VAT is')
print (total)