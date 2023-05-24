#Задача 2: Найдите сумму цифр трехзначного числа.
n = int(input("Введите трехназное число: "))
while n < 100 or n > 999:
    n = int(input("Неверное число.Введите трехзначное число: "))
n1 = n // 100
n2 = (n % 100) // 10
n3 = n % 10
print(n1 + n2 + n3)

#Задача 4:
n = int(input("Введите общее количество журавликов:"))
sergey = n / 6
petr = sergey
ekaterina = (sergey + petr) * 2
print(int(sergey), int(ekaterina), int(petr))

#Задача 6:
n = int(input("Введите номер билета: "))
a=n // 1000
b=n % 1000
d1=a // 100
d2=a % 100//10
d3=a % 10
sum1=d1+d2+d3
print("Сумма первых трех чисел--->",sum1)
d4=b // 100
d5=b % 100//10
d6=b % 10
sum2=d4+d5+d6
print ("Сумма последних трех чисел--->",sum2)
if sum1 == sum2:
  print("YES, ВЫИГРЫШ")
else:
  print("NO, ПРОИГРЫШ")
  
#Задача 8:
n = int(input("Введите ширину шоколадки: "))
m = int(input("Введите длину шоколадки: "))
k = int(input("Введите сколько долек Вам нужно: "))
if k < m*n and (k%m==0 or k%n==0):
    print('YES')
else:
    print('NO')