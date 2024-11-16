# 1) Найти все числа от 1 до 1000, которые делятся на 7
a = [i for i in range(1, 1001) if i % 7 == 0]
print(a)


# 2) Сгенерировать список на основе чисел от 1 до 1000.
# Если число делится на 3 - положить результат деления в коллецию без изменений,
# в противном случае положить число записанное дважды друг за другом
b = []
for i in range(1, 1001):
    if i % 3 == 0:
        b.append(i)
    else:
        b.append(int(str(i) * 2))
print(b)


# 3) Посчитать кол-во пробелов в строке "  hel l o      world   "
hel_wor = "  hel l o      world   "
result = hel_wor.count(" ")
print(result)


# 4) Сгенерировать список из слов строки
# “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”,
# которые начинаются на Y/y
current_str = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
k = current_str.split(" ")
res = [i for i in k if i.startswith("Y") or i.startswith("y")]
print(res)


# 5) Для каждого элемента строки  "hi, 3.44, 535  "
# сгенерировать коллекцию кортежей вида (индекс, значение), (индекс, значение)
z = []
first_str = "hi, 3.44, 535  "
second_str = first_str.split(",")
h = [i.strip() for i in second_str]
for i in h:
    z.append((h.index(i), i))
print(z)


# 6) Сгенерировать коллекцию с числами из
# строки "In 1984 there were 13 instances of a protest with over 1000 people attending"
base_str = "In 1984 there were 13 instances of a protest with over 1000 people attending"
g = base_str.split(" ")
res_list = [i for i in g if i.isnumeric()]
print(res_list)


# 7) Для чисел из промежутка [1, 20] сгенерировать коллекцию строк вида ("четное", "нечетное", "четное")
t = [1, 20]
r = []
for i in range(t[0], t[1] + 1):
    if i % 2 == 0:
        r.append("четное")
    else:
        r.append("нечетное")
res_tup = tuple(r)
print(res_tup)


# 8) Найти все слова из строки, длина которых меньше 4
# символов "The trickiest part of learning list comprehension for me was really understanding the syntax."
my_string = "The trickiest part of learning list comprehension for me was really understanding the syntax."
y = my_string.split(" ")
w = [i for i in y if len(i) <= 4]
print(w)


# 9) Найти простые числа из промежутка [1, 50].
# Простым числом называется число, которое делится только на единицу и на себя же.
period = [1, 50]
my_list = [i for i in range(period[0], period[1] + 1) if i > 1 and all(i % j != 0 for j in range(2, i))]
print(my_list)
