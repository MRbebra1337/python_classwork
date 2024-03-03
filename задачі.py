
#zadacha1
print("Введіть ваше імя: ")
name = input()
print("Вітаю, ", name)

#zadacha2
age = int(input("Введіть свій вік: "))

if age >= 18 :
   print("Ви дорослий і крутий крутелик")
else:
    print("Ви ще маленькі ідіть дивіться гумку боба")
#zadacha3
chislo = int(input("Введіть число бистро !!!!: "))

if chislo < 0 :
    print(chislo * -1)
else:
    print(chislo)
#zadacha4
password = input("Пароль сюда швиденько: ")
password2 = input("ТЕпер ше раз пжпжпжпж: ")
if password==password2:
    print("тепер я вкраду вашу ветчину з холодильника")
else:
    print("ви олушара введіть правільно")
#zadacha5
number = int(input("Введіть число пж: "))
number2 = int(input("Введіть 2 число : "))
if number>number2:
    print(number , "більше")
else:
    print(number2, "більше")
#zadacha6
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
num3 = int(input("Введіть третє число: "))
average = (num1 + num2 + num3) / 3
print("Середнє значення:", average)
#zadacha7
length = int(input("Введіть довжину прямокутника: "))
width = int(input("Введіть ширину прямокутника: "))
area = length * width
perimeter = 2 * (length + width)
print("Площа прямокутника:", area)
print("Периметр прямокутника:", perimeter)
#zadacha8
number = int(input("Введіть число від 1 до 7: "))
if number == 1:
    print("Понеділок")
elif number == 2:
    print("Вівторок")
elif number == 3:
    print("Середа")
elif number == 4:
    print("Четвер")
elif number == 5:
    print("П'ятниця")
elif number == 6:
    print("Субота")
elif number == 7:
    print("Неділя")
else:
    print("ну олух введи число від 1 до 7")
#zadacha9
number = int(input("Введіть число: "))
if number % 2 == 0:
    print("Число парне")
else:
    print("Число не парне")
#zadacha10
def can_break_chocolate(n, m, k):
    total_pieces = n + m - 2
    if k >= 0 and k <= total_pieces:
        return True
    else:
        return FalseS
n=int(input("Введіть кількість рядків шоколадки (п): "))
m=int(input("Введіть кількість стовпчиків заколадки (п): "))
k=int(input("Введіть бажану кількість частинок (к): "))
if can_break_chocolate(n ,m ,k):
    print("Tак,можна отримати рівно ", k, "частинок шоколадки. ")