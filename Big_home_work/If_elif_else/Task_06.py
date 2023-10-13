# Дан номер месяца (число от 1 до 12). Выведите пору года,
# которой этот месяц принадлежит: зима, весна, лето или осень.
month = int(input('Enter the month number.'))
if 2 < month < 6:
    print('весна')
elif 5 < month < 9:
    print('лето')
elif 8 < month < 12:
    print('осень')
else:
    print('зима')
