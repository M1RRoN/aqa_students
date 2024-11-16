# 1) Найти все числа от 1 до 1000, которые делятся на 7
a = [i for i in range(1, 1001) if i % 7 == 0]
print(a)


# 2) Сгенерировать список на основе чисел от 1 до 1000.
# Если число делится на 3 - положить результат деления в коллецию без изменений,
# в противном случае положить число записанное дважды друг за другом
b = [i if i % 3 == 0 else int(str(i) * 2) for i in range(1, 1001)]
print(b)


# 3) Посчитать кол-во пробелов в строке "  hel l o      world   "
hel_wor = "  hel l o      world   "
result = sum(1 for i in hel_wor if i == " ")
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
first_str = "hi, 3.44, 535  "
z = [(i, value) for i, value in enumerate([i.strip() for i in first_str.split(",")])]
print(z)


# 6) Сгенерировать коллекцию с числами из
# строки "In 1984 there were 13 instances of a protest with over 1000 people attending"
base_str = "In 1984 there were 13 instances of a protest with over 1000 people attending"
g = base_str.split(" ")
res_list = [i for i in g if i.isnumeric()]
print(res_list)


# 7) Для чисел из промежутка [1, 20] сгенерировать коллекцию строк вида ("четное", "нечетное", "четное")
t = [1, 20]
r = tuple(["четное" if i % 2 == 0 else "нечетное" for i in range(t[0], t[1] + 1)])
print(r)


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
