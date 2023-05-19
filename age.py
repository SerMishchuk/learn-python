def check_age(age):
   if age < 7:
    return 'Вам еще надо походить в детский сад!'
   elif age >= 7 and age <18:
    return 'Вам нужно ходить в школу.'
   elif age >= 18 and age <23:
    return 'Вам нужно ходить в ВУЗ.'
   elif age >= 23 and age < 30:
    return 'Вам уже пора идти на работу!'
   else:
    return 'Иди на работу!'
   
age = input("Сколько вам лет? ")
age = int(age)
print(check_age(age))

