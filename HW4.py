# 4. Apgriezt pozitīva skaitļa ciparu secību.

# num1 = input('Enter number:')
# num2 = num1[::-1]
# print('"Reversed" number:', num2)

num1 = input('Enter number:')
list = list(num1)
list.reverse()
num2 = "".join(list)
print('"Reversed" number:', num2)
