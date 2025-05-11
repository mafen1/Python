# списки
import math
import re

# 3 задание

list = [3, -54, 25, 8, 0]

print(max(list) - min(list))
print(sum(list))

# 5 задание

list1 = [1, 22, 13, 4]
list2 = [10, 13, 21, 4]

for i in list1:
    for j in list2:
        if i == j:
            print(i)

# через множества
print(({1, 22, 13, 4} & {10, 13, 21, 4}))

# 6 задание

list3 = [1, 2, 3, 4, 5]
newList = []
for i in list3:
    newList.append(math.pow(i, 2))
print(newList)

# Строки

# задание 1

string = "How many characters are there?"
count = 0
for i in string:
    if i == "a":
        count += 1
print(count)

# сокращенный вариант

print("How many characters are there?".count("a"))

# 2 задание

str2 = "Hi, how are you? I thought you left!"
print(re.sub(r'[.,!?;:]', '', string))

# 6 задание

string = "abc"
result = ''.join(c * 2 for c in string)
print(result)  # Вывод: "aabbcc"

# Циклы

# Задача 2

listPeople = [1234, 5678, 9012, 3456, 7890, 1122, 3344, 5566, 7788, 9901, 2001, 4500]
listArea = [123456, 789012, 345678, 901234, 567890, 111222, 333444, 555666, 777888, 999001, 456789, 123456]

resultPeople = 0
resultArea = 0

for i in listPeople:
    resultPeople += i

for j in listArea:
    resultArea += j

print(resultPeople / resultArea)

# Задача 3

km = 10
total_7_days = km
listDay = ["второй", "третий", "четвертый", "пятый",
              "шестой", "седьмой", "восьмой", "девятый", "десятый"]

for day in range(1, 10):
    km *= 1.1
    print(f"{listDay[day - 1]} день: {km:} км")
    if day < 7:  # Учитываем первые 7 дней
        total_7_days += km

print(f"Суммарный путь за первые 7 дней: {total_7_days:} км")

# Задача 4

b = int(input("Введите число b: "))
d = int(input("Введите число d: "))

start = min(b, d)
end = max(b, d)

total = 0
count = 0

for num in range(start, end + 1):
    total += num
    count += 1

middle = total / count
print(f"Среднее арифметическое от {b} до {d}: {middle}")
