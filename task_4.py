# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#Первое решение
n = int(input('Введите число'))
binar = 0
i=0
while n >= 1:
    binar = binar + (n%2*(10**i))
    i+=1
    n//=2
print(binar)

##Второе Решение
# print(bin(n))

###Третье решение
# number = int(input('Введите число: '))
 
# numberb = ''
 
# while number > 0:
#     numberb = str(number % 2) + numberb
#     number//= 2
 
# print(numberb)