# money = int(input("Enter value in cents: "))
#
# one_cent = 1
# five_cent = 5
# ten_cent = 10
# tweny_five_cent = 25
# loonie = 100
# toonie = 200
#
# toonies_quantity = money // toonie
# money %= toonie
#
# loonies_quantity = money // loonie
# money %= loonie
#
# tweny_five_cent_quantity = money // tweny_five_cent
# money %= tweny_five_cent
#
# ten_cent_quantity = money // ten_cent
# money %= ten_cent
#
# five_cent_quantity = money // five_cent
# money %= five_cent
#
# one_cent_quantity = money // one_cent
# one_cent_quantity = money % five_cent
#
# result = f"""toonies: {toonies_quantity}
# loonies: {loonies_quantity}
# 25 cent: {tweny_five_cent_quantity}
# 10 cent: {ten_cent_quantity}
# 5 cent: {five_cent_quantity}
# 1 cent {one_cent_quantity}"""
#
# print(result)

# celsius = int(input("Enter celsius"))
#
# fahrenheit = (celsius * 9/5) + 32
#
# print(f"{fahrenheit:.2f}F")


# seconds = int(input("Enter time in seconds: "))
#
# time_on_days = seconds // 86400
# seconds %= 86400
#
# time_on_hours = seconds // 3600
# seconds %= 3600
#
# time_on_minutes = seconds // 60
# seconds %= 60
#
# result = f"{time_on_days:02d}:{time_on_hours:02d}:{time_on_minutes:02d}"
#
# print(result)

# x = int(input("Enter x cordinat: "))
# y = int(input("Enter y cordinat: "))
#
# if x<y:
#     print(f"{y} is maximum")
# else:
#     print(f"{x} is maximum")


# balance = 20000
# value = int(input(">>> "))
#
# if balance < 20000:
#     if value <= balance * 400:
#         print(f"you have 10% discount you can change your {value} to usd")
#     else: print("you dont have enough money")
# elif balance >= 20000:
#     if value >= balance * 400:
#         print("you dont have enough money")
# else: print(f"you can change your {value} to usd")


# year = int(input(">>> "))
#
# a = year % 19
# b = year // 100
# c = year % 100
# d = b // 4
# e = b % 4
# f = (b + 8) // 25
# g = (b - f + 1) // 3
# h = (19 * a + b - g + 15) % 30
# i = c //4
# k = c % 4
# l = (32 + 2 * e + 2 * i - h - k) % 7
# m = (a + 11 * h + 22 * l) // 451
# month = (h + l - 7 * m + 144) / 31
# day = 1 + ((h + l - 7 * m + 144) % 31)
#
# print(f"{day:02d}:{month:02d}:{year:4d}")

# field = input("Enter field in chess")
# column = field[0]
# row = field[1]
# if column in "aceg" and int(row) % 2 != 0\
#     or column in "bdfh" and int(row) % 2 == 0:
#     print("black")
# else:
#     print("white")


# tarif = 15
# sms = int(input(">>> "))
# minutes = int(input(">>> "))
# after_tarif_minutes = 0.25
# after_tarif_sms = 0.15
# call_centre = 0.44
#
# if sms > 50 or minutes > 50:
#     print(f"base plan: {tarif:.2f}$")
#     print(f"sms price: {(sms - 50) * after_tarif_sms}$")
#     print(f"minutes price: {(minutes - 50) * after_tarif_minutes}$")
#     print(f"call centre: {call_centre}$")

# plate_number = input("Enter license plate number")
# plate_number_length = len(plate_number)
#
# if plate_number_length != 6 and plate_number_length !=7:
#     print("Enter a correct plate number")
# if plate_number[:3].isalpha() and plate_number[3:].isdigit():
#     print("old format")
# elif plate_number[:4].isalpha() and plate_number[4:].isdigit():
#     print("new format")
# else:
#     print()


# num = int(input("Enter first number: "))
# num_1 = int(input("Enter second number: "))
# if num > num_1:
#     print(num)
# elif num == num_1:
#     print(f"numbers are havasar")
# else:
#     print(num_1)



# num = int(input("Enter first number: "))
# num_1 = int(input("Enter second number: "))
# num_2 = int(input("Enter third number"))
#
# if num < num_1 and num < num_2:
#     print(num)
# elif num_1 < num and num_1 < num_2:
#     print(num_1)
# else:
#     print(num_2)

# num = int(input("Enter number: "))
#
# count = 0
#
# while num:
#     count *= 10
#     num_1 = num % 10
#     count += num_1
#     num //= 10
#
# print(count)

# Age = int(input("Enter Age: "))
# Ser = input("M or F: ")
# Marriage = input("Y or N: ")
#
# if Ser == "F":
#     print("You will work only in urban areas")
# elif Ser == "M" and 20 <= Age <= 40:
#     print("You may work anywhere")
# elif Ser == "M" and 40 <= Age <= 60:
#     print("You will work only urban areas")
# elif Age < 20 or Age > 60:
#     print("ERROR")

# import random
#
# combinacia = "rock", "paper", "sisers"
#
# pc_choice = random.choice(combinacia)
#
# print(pc_choice)

