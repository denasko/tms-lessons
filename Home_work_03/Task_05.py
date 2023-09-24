months = {"january": 31, "february": 28, "march": 31,
          "april": 30, "may": 31, "june": 30, "july": 31,
          "august": 31, "september": 30, "october": 31,
          "november": 30, "december": 31}


def how_many_days_in_month(month):
    if month in months:
        return months.get(month)
    else:
        print("Ошибка,проверьте введенные данные:")
        return month


month = input("Введите название месяца на английском языке.").lower()
print(how_many_days_in_month(month))
