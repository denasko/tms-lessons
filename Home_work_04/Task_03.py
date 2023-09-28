break_out = False
for i in range(101):
    flag = True
    while flag:
        answer = input('Should we break?')
        if answer == 'yes':
            flag = False
            break_out = True
            break
        elif answer == "no":
            print(i)
            flag = False
        else:
            print("Don't understand you")
    if break_out == True:
        break
# Сломал себе голову,как можно сделать задание без флага.Если не сложно,укажите
# где можно упростить :(
# Я уже понял свою ошибку) Я почемуто убедил себя в необходимости использования рэндж и вложенного цикла) можно сделать одним вайл,но я уже оставлю как есть.
